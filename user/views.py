from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from home.models import Setting, Client
from product.models import Category, Product
# Create your views here.

@login_required(login_url='/login')
def userprofile(request):
    # current_user = request.user
    # profile= UserProfile.objects.get(user_id=current_user.id)
    profile = UserProfile.objects.filter(user_id=request.user.id).first()
    #profile = UserProfile.objects.get_or_create(user_id=request.user.id)
    userform = UserUpdateForm(instance=request.user)
    profileform = ProfileUpdateForm(instance=request.user.userprofile)
    if request.method == 'POST':
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if userform.is_valid and profileform.is_valid:
            userform.save()
            profileform.save()
            return redirect('index')

    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.userprofile)
        setting= Setting.objects.get(pk=1)
        clients = Client.objects.all()
        category = Category.objects.all()
        bestseller = Product.objects.filter(bestseller= True)[:6]
        topseller = Product.objects.filter(topseller =True)[:6]
        trending = Product.objects.filter(trending =True)[:6]
        featured = Product.objects.filter(featured= True)[:6]
        latest = Product.objects.filter(latest= True)[:6]
        

        context = {
            # 'userform': userform,
            # 'profileform': profileform,
            'profile': profile,
            'setting': setting,
            'clients': clients,
            'category': category,
            'bestseller': bestseller,
            'topseller': topseller,
            'trending': trending,
            'latest': latest,
        }
    return render(request, 'userprofile.html', context)
    



def loginform(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user=request.user
            userprofile= UserProfile.objects.get(user_id=current_user.id)
            #profile= UserProfile.objects.get_or_create(user_id=current_user.id)
            request.session['userimage']= userprofile.image.url

            # redirect to a success page
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('index')
        else:
            
            messages.warning(request,"Login Error! Invalid Username or Password")
            return redirect('loginform')

    setting= Setting.objects.get(pk=1)
    clients = Client.objects.all()
    category = Category.objects.all()
    bestseller = Product.objects.filter(bestseller= True)[:6]
    topseller = Product.objects.filter(topseller =True)[:6]
    trending = Product.objects.filter(trending =True)[:6]
    latest = Product.objects.filter(latest= True)[:6]
    

    context = {
            'setting': setting,
            'clients': clients,
            'category': category,
            'bestseller': bestseller,
            'topseller': topseller,
            'trending': trending,
            'latest': latest,
    }
    return render(request, 'loginform.html', context)
        
    
def logoutfunc(request):
    logout(request)
    return redirect('index')


def signupform(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            myuser = form.save()
            p = UserProfile(user=myuser)
            p.first_name= myuser.first_name
            p.last_name= myuser.last_name
            p.save()
            # UserProfile.objects.create(user=myuser)
            # username= form.cleaned_data.get("username")
            # password= form.cleaned_data.get("password1")
            # user = authenticate(username=username, password=password)
            login(request, myuser)
            return redirect('index')
        else:
            messages.warning(request,form.errors)
            return redirect('signupform')

    setting= Setting.objects.get(pk=1)
    clients = Client.objects.all()
    category = Category.objects.all()
    bestseller = Product.objects.filter(bestseller= True)[:6]
    topseller = Product.objects.filter(topseller =True)[:6]
    trending = Product.objects.filter(trending =True)[:6]
    featured = Product.objects.filter(featured= True)[:6]
    latest = Product.objects.filter(latest= True)[:6]


    context = {
        'form':form,
        'setting': setting,
        'clients': clients,
        'category': category,
        'bestseller': bestseller,
        'topseller': topseller,
        'trending': trending,
        'latest': latest,
    }
    return render(request, 'signupform.html', context)


@login_required(login_url='/login')
def userupdate(request):
    if request.method == 'POST':
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if userform.is_valid and profileform.is_valid:
            userform.save()
            profileform.save()
            messages.success(request, 'Your Account has been updated!')
            return redirect('user')
    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.userprofile)
        setting= Setting.objects.get(pk=1)
        clients = Client.objects.all()
        category = Category.objects.all()
        bestseller = Product.objects.filter(bestseller= True)[:6]
        topseller = Product.objects.filter(topseller =True)[:6]
        trending = Product.objects.filter(trending =True)[:6]
        featured = Product.objects.filter(featured= True)[:6]
        latest = Product.objects.filter(latest= True)[:6]

        context = {
            'userform': userform,
            'profileform': profileform,
            'setting': setting,
            'clients': clients,
            'category': category,
            'bestseller': bestseller,
            'topseller': topseller,
            'trending': trending,
            'latest': latest,
        }
    return render(request, 'userupdate.html', context)



@login_required(login_url='/login')
def userpassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user')

        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return redirect('userpassword')
    else:
        form = PasswordChangeForm(request.user)
        setting= Setting.objects.get(pk=1)
        clients = Client.objects.all()
        category = Category.objects.all()
        bestseller = Product.objects.filter(bestseller= True)[:6]
        topseller = Product.objects.filter(topseller =True)[:6]
        trending = Product.objects.filter(trending =True)[:6]
        featured = Product.objects.filter(featured= True)[:6]
        latest = Product.objects.filter(latest= True)[:6]

        context = {
            'form': form,
            'setting': setting,
            'clients': clients,
            'category': category,
            'bestseller': bestseller,
            'topseller': topseller,
            'trending': trending,
            'latest': latest,
        }
    return render(request, 'userpassword.html', context)

#for account delete
# def delete_acct_confirm(request):
#     return render(request, 'delete_acct_confirm.html')

def delete_acct(request):
    theuser = User.objects.get(pk=request.user.id)
    logout(request)
    theuser.delete()
    return redirect('index')