from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from home.models import Setting
from product.models import Category, Product
from .models import ShopCart, ShopCartForm
from user.models import UserProfile
from django.contrib.auth.decorators import login_required
# from django.utils.crypto import get_random_string
from order.models import Order, OrderForm, OrderProduct, ShopCart
import requests
import json
import random
import string
from django.contrib.auth.models import User
import uuid
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return HttpResponse('New App')
 
@require_POST
@login_required(login_url='/login')
def addtoshopcart(request):
    url = request.META.get('HTTP_REFERER')
    thequantity = int(request.POST['quantity'])
    theprodid = request.POST['prodid']
    aprod = Product.objects.get(pk=theprodid)

    #check if the user has an existing cart
    cart= ShopCart.objects.filter(order_placed=False).filter(user__username = request.user.username)

    if cart: #an existing
        prodchecker = ShopCart.objects.filter(product_id = aprod.id).filter(user__username = request.user.username).first()

        if prodchecker: #porduct exists in the cart, increment it
            prodchecker.quantity += thequantity
            prodchecker.save()
            messages.success(request, "Product added to ShopCart")
            return redirect(url)

        else: #product is not in the cart, add it
            anitem = ShopCart()
            anitem.product=aprod
            anitem.user=request.user
            anitem.order_code=cart[0].order_code
            anitem.quantity=thequantity
            anitem.order_placed=False
            anitem.save()
    
    else: #create a new cart, generate order number
        ordercode = str(uuid.uuid4())
        newcart = ShopCart()
        newcart.product=aprod
        newcart.user=request.user
        newcart.order_code=ordercode
        newcart.quantity=thequantity
        newcart.order_placed=False
        newcart.save()
    
    messages.success(request, "Product added to ShopCart")
    return redirect(url)




# @require_POST
# @login_required(login_url='/login')
# def addtoshopcart(request):
#     url = request.META.get('HTTP_REFERER')
#     thequantity = 
#     current_user = request.user

#     checkproduct = ShopCart.objects.filter(product_id=id)
#     if checkproduct:
#         control = 1

#     else:
#         control = 0
    
#     if request.method == "POST":
#         form = ShopCartForm(request.POST)
#         if form.is_valid():
#             if control==1:
#                 data=ShopCart.objects.get(product_id=id)
#                 data.quantity += form.cleaned_data['quantity']
#                 data.save()
#             else:
#                 data = ShopCart()
#                 data.user_id=current_user.id
#                 data.product_id=id
#                 data.quantity = form.cleaned_data['quantity']
#                 data.save()
#         messages.success(request, "Product added to Shopcart")
#         return redirect(url)
    
#     else:
#         if control==1:
#             data=ShopCart.objects.get(product_id=id)
#             data.quantity += 1
#             data.save()
#         else:
#             data = ShopCart()
#             data.user_id = current_user.id
#             data.product_id=id
#             data.quantity = 1
#             data.save()
#     messages.success(request, "Product added to Shopcart")
#     return redirect(url)

def shopcart(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    randomize = Product.objects.filter(featured=True)[:1]
    total= 0
    shippingfee = 0
    val = 0
    grandtotal = 0

    for item in shopcart:
        total += item.product.price * item.quantity
    
    #Shipping rules: 8% fees to all orders above 150. 0 fees to orders lower
    if total > 150:
        shippingfee = 0.08 * total
    else:
        shippingfee = 0
    
    vat = 0.075 * total
    
    grandtotal = total +  shippingfee + vat

    context = {
        'setting':setting,
        'category': category,
        'shopcart': shopcart,
        'randomize': randomize,
        'total': total,
        'shipping':shippingfee,
        'vat': vat,
        'grandtotal': grandtotal
    }
    return render(request, 'shopcart.html', context)

@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'Item deleted from Shopcart')
    return redirect('order:shopcart')


@login_required(login_url='/login')
def checkout(request):
    category = Category.objects.all()
    #current_user = request.user
    shopcart = ShopCart.objects.filter(user__username = request.user.username).filter(order_placed=False)
    profile = UserProfile.objects.get(user__username = request.user.username)
    randomize = Product.objects.filter(featured=True)[:1]
    total = 0
    shippingfee = 0
    vat = 0
    grandtotal = 0

    for item in shopcart:
        if item.product.discount_price:
            total += item.product.discount_price * item.quantity
        else:
            total += item.product.price * item.quantity
    
    #Shipping rules: 8% fees to all orders above 150. 0 fees to orders lower
    if total > 150:
        shippingfee = 0.08 * total
    else:
        shippingfee = 0
    
    #vat is at 7.50% of the total purchase to be made
    vat = 0.075 * total

    grandtotal = total + shippingfee + vat

    # if request.method == "POST":
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         # configure payment gateway here
    #         data= form.save()
    #         data = Order()
    #         data.first_name = form.cleaned_data['first_name']
    #         data.last_name = form.cleaned_data['last_name']
    #         data.address = form.cleaned_data['address']
    #         data.city = form.cleaned_data['city']
    #         data.phone = form.cleaned_data['phone']
    #         data.user_id = current_user.id
    #         data.total=total
    #         data.ip = request.META.get('REMOTE_ADDR')
    #         ordercode = get_random_string(5).upper()
    #         data.code = ordercode
    #         data.save()
            
    #         #move shopcart items to order-product table
    #         shopcart = ShopCart.objects.filter(user_id=current_user.id)
    #         for item in shopcart:
    #             detail = OrderProduct()
    #             detail.order_id = data.id
    #             detail.product_id = item.product_id
    #             detail.user_id = current_user.id
    #             detail.quantity = item.quantity
    #             detail.price = item.product.price
    #             detail.amount = item.amount
    #             detail.save()

    #             # remove quantity of sold product from amount of product
    #             product = Product.objects.get(id= item.product_id)
    #             product.number -= item.quantity
    #             product.save()

    #         #clear and delete shopcart
    #         ShopCart.objects.filter(user_id=current_user.id).delete()
    #         request.session['cart.items']=0
    #         messages.success(request, 'Your order has been completed. Thank you')
    #         return render (request, 'ordercompleted.html', {'ordercode':ordercode, 'profile':profile, 'category':category})
    #     else:
    #         messages.warning(request, form.errors)
    #         return redirect('order:orderproduct')

    

    context = {
        'shopcart':shopcart,
        'order_code': shopcart[0].order_code,
        'profile': profile,
        'category':category,
        'randomize':randomize,
        'total':total,
        'shipping':shippingfee,
        'vat':vat,
        'grandtotal':grandtotal,
    }

    return render(request, 'checkout.html', context)


@require_POST
@login_required(login_url='/login')
def placeorder(request):
    api_key = 'sk_test_4928f50a0c9ae1263e2be83d0a6cca93030948bd'
    url = 'https://api.paystack.co/transaction/initialize'
    callback_url = 'http://localhost:8000/order/ordercompleted'
    # ordercode = 'ordercode' in request.POST and request.POST['ordercode']
    ordercode = request.POST['order_number']
    autogen_ref = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
    current_user = User.objects.get(username = request.user.username)
    user = UserProfile.objects.get(user_id = current_user.id)
    total = float(request.POST['amount']) * 100
    

    headers = {'Authorization': f'Bearer {api_key}'}
    data = {'reference': autogen_ref, 'amount': int(total), 'order_number': ordercode, 'email': user.email, 'callback_url': callback_url}

    # making a request to PAYSTACK
    try:
        r = requests.post(url, headers=headers, json=data)
    except Exception:
        messages.error(request, 'Network busy, Please try again in a few minutes. Thanks')
    else:
        #create an order
        transback = json.loads(r.text)

        rd_url = transback['data']['authorization_url']
        theuser = UserProfile.objects.filter(user=request.user).first()
        order = Order()
        order.first_name = theuser.user.first_name
        order.last_name = theuser.user.last_name
        order.phone=theuser.phone
        order.city=theuser.city
        order.order_code=ordercode
        order.total=total
        order.order_placed = True
        order.save()
        return redirect(rd_url)
    return redirect('order:checkout')

@login_required(login_url='/login')
def ordercompleted(request):
    shopcart =ShopCart.objects.filter(user__username = request.user.username).filter(order_placed=False)
    profile = UserProfile.objects.get(user__username = request.user.username)
    #cleaning the shopcart
    for item in shopcart:
        item.order_placed = True
        item.save()


        #reducing quantity instock
        aproduct = Product.objects.get(id=item.product.id)
        aproduct.quantity_instock -= item.quantity
        aproduct.save()

    total= 0
    shippingfee = 0
    val = 0
    grandtotal = 0

    for item in shopcart:
        total += item.product.price * item.quantity
    
    #Shipping rules: 8% fees to all orders above 150. 0 fees to orders lower
    if total > 150:
        shippingfee = 0.08 * total
    else:
        shippingfee = 0
    
    vat = 0.075 * total
    
    grandtotal = total +  shippingfee + vat

    context = {
        'shopcart': shopcart,
        'profile': profile,
        'order_code': shopcart[0].order_code,
        'total': total,
        'shipping':shippingfee,
        'vat': vat,
        'grandtotal': grandtotal
    }
    return render(request, 'ordercompleted.html')
    

