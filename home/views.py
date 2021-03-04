from django.shortcuts import render

from django.contrib import messages
from .models import Setting,ContactForm,ContactMessage, Client, Slider
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Category, Product, Images
from user.models import UserProfile

  
# Create your views here.
def index(request):
    setting= Setting.objects.get(pk=1)
    clients = Client.objects.all()
    slider = Slider.objects.get(pk=2)
    category = Category.objects.all()
    bestseller = Product.objects.filter(bestseller= True)[:8]
    topseller = Product.objects.filter(topseller =True)[:8]
    trending = Product.objects.filter(trending =True)[:8]
    featured = Product.objects.filter(featured= True).order_by('-id')[:8]
    latest = Product.objects.filter(latest= True)[:8]
    prod_feature = Product.objects.filter(featured= True)[:4]
    prod_latest = Product.objects.filter(latest= True)[:4]
    profile = UserProfile.objects.filter(user_id=request.user.id).first()

    context={
        'setting':setting,
        'clients': clients,
        'slider': slider,
        'category': category,
        'bestseller': bestseller,
        'topseller': topseller,
        'trending': trending,
        'featured': featured,
        'latest': latest,
        'prod_feature': prod_feature,
        'prod_latest': prod_latest,
        'profile':profile,
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Hello world")

def about(request):
    setting = Setting.objects.get(pk=1)
    clients = Client.objects.all()
    category = Category.objects.all()
    bestseller = Product.objects.filter(bestseller= True)[:6]
    topseller = Product.objects.filter(topseller =True)[:6]
    trending = Product.objects.filter(trending =True)[:6]
    featured = Product.objects.filter(featured= True)[:6]
    latest = Product.objects.filter(latest= True)[:6]
    context= { 'setting': setting,
                'clients': clients,
                'category': category,
                'bestseller': bestseller,
                'topseller': topseller,
                'trending': trending,
                'featured': featured,
                'latest': latest,
     }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            form.save()
            messages.success(request,"Your message has been sent! Our Customer Service Team Will reach you soon.")
            return HttpResponseRedirect('/contact')


    setting = Setting.objects.get(pk=1)
    form = ContactForm
    clients = Client.objects.all()
    category = Category.objects.all()
    bestseller = Product.objects.filter(bestseller= True)[:6]
    topseller = Product.objects.filter(topseller =True)[:6]
    trending = Product.objects.filter(trending =True)[:6]
    featured = Product.objects.filter(featured= True)[:6]
    latest = Product.objects.filter(latest= True)[:6]
    
    context= { 'setting': setting,
                'form': form,
                'clients': clients,
                'category': category,
                'bestseller': bestseller,
                'topseller': topseller,
                'trending': trending,
                'featured': featured,
                'latest': latest,
                
     }
    return render(request, 'contact.html', context)
    

def refrences(request):
    setting = Setting.objects.get(pk=1)
    clients = Client.objects.all()
    category = Category.objects.all()
    bestseller = Product.objects.filter(bestseller= True)[:6]
    topseller = Product.objects.filter(top_seller =True)[:6]
    trending = Product.objects.filter(trending =True)[:6]
    featured = Product.objects.filter(featured= True)[:6]
    latest = Product.objects.filter(latest= True)[:6]
    context= { 'setting': setting,
                'clients': clients,
                'category': category,
                'bestseller': bestseller,
                'topseller': topseller,
                'trending': trending,
                'featured': featured,
                'latest': latest,
    }
    return render(request, 'refrences.html', context)


def category_prod(request,id,slug):
    setting= Setting.objects.get(pk=1)
    clients = Client.objects.all()
    category = Category.objects.all()
    catdata= Category.objects.get(pk=id)
    bestseller = Product.objects.filter(bestseller= True)[:6]
    topseller = Product.objects.filter(topseller =True)[:6]
    trending = Product.objects.filter(trending =True)[:6]
    featured = Product.objects.filter(featured= True)[:6]
    latest = Product.objects.filter(latest= True)[:6]
    randomize = Product.objects.filter(bestseller= True)[:1]
    randomise = Product.objects.filter(topseller =True)[:1]
    bestseller = Product.objects.filter(latest= True)[:3]
    products = Product.objects.filter(category_id=id)


    context= {
                'setting': setting,
                'clients': clients,
                'category': category,
                'catdata': catdata,
                'bestseller': bestseller,
                'topseller': topseller,
                'trending': trending,
                'featured': featured,
                'latest': latest,
                'randomize': randomize,
                'randomise': randomise,
                'bestseller': bestseller,
                'products': products,

     }
    return render(request, 'category_prod.html', context)
    # return HttpResponse(products)



def prod_detail(request,id,slug):
    setting= Setting.objects.get(pk=1)
    clients = Client.objects.all()
    category = Category.objects.all()
    bestseller = Product.objects.filter(bestseller= True)[:6]
    topseller = Product.objects.filter(topseller =True)[:6]
    trending = Product.objects.filter(trending =True)[:6]
    featured = Product.objects.filter(featured= True)[:6]
    latest = Product.objects.filter(latest= True)[:6]
    randomize = Product.objects.filter(topseller= True)[:1]
    randomise = Product.objects.filter(featured =True)[:1]
    bestseller = Product.objects.filter(latest= True)[:3]
    products = Product.objects.filter(category_id=id)
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)


    context= {
                'setting': setting,
                'clients': clients,
                'category': category,
                'bestseller': bestseller,
                'topseller': topseller,
                'trending': trending,
                'featured': featured,
                'latest': latest,
                'randomize': randomize,
                'randomise': randomise,
                'bestseller': bestseller,
                'products': products,
                'product': product,
                'images': images
     }
    return render(request, 'prod_detail.html', context)