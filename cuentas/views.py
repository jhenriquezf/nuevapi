from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from cuentas.models.product import Product


# Create your views here.
def home(request):
    return render (request,'home.html')


def signup(request):
    if request.method =='GET':
        return render (request,'signup.html',{
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('cuentas')
            except IntegrityError:
                return render (request,'signup.html',{
                    'form' : UserCreationForm,
                    "error": 'Username already exists'
                })
        return render (request,'signup.html',{
            'form' : UserCreationForm,
            "error": 'Password do not match'
        })    

def cuentas(request):
    return render (request,'cuentas.html')

def create_cuenta(request):
    products = Product.objects.all()
    return render (request,'create_cuenta.html',{'products':products})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Password incorrecto'
            })
        else:
            login(request, user)
            return redirect('cuentas')


