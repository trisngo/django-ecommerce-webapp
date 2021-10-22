from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Profile, User
from django.contrib import messages
from django.urls import reverse

# get index page
def index_view(request):
    return render(
        request,
        'index.html', 
        {
            
        }
    )
# get product page
def product_view(request):
    return render(
        request,
        'product-single.html', 
    )

# get shop page
def shop_view(request):
    return render(
        request,
        'shop.html', 
    )

# get login page
def login_view(request):
    if request.method == 'POST':
        if 'phone' not in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            print(username)
            print(password)
            
            try: 
                user = User.objects.get(username=username) #query của django
                print(user)
            except:
                messages.error(request, 'User does not exist')
                return redirect('login')
                
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username or Password is wrong')
                return redirect('login')
        else:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            name = request.POST['name']
            phone = request.POST['phone']
            address = request.POST['address']

            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Used')
                    return redirect('login')
                elif User.objects.filter(username=username).exists():
                    messages.error(request, 'Username Already Used')
                    return redirect('login')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.is_active = True
                    user.first_name = name
                    user.profile.address = address
                    user.profile.phone = phone
                    user.save()
                    return redirect('home')
            else:
                messages.info(request, 'Password is not same')
                return redirect('login')
    else:
        return render(request, 'login.html')



# get contact page
def contact_view(request):
    return render(
        request,
        'contact.html',
    )

# get about page
def about_view(request):
    return render(
        request,
        'about.html',
    )

# get cart page
def cart_view(request):
    return render(
        request,
        'cart.html',
    )

# get checkout page
def checkout_view(request):
    return render(
        request,
        'checkout.html',
    )

# get wishlist page
def wishlist_view(request):
    return render(
        request,
        'wishlist.html',
    )
