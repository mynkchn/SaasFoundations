from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate 
from django.contrib import messages
from cfehome.views import home_page_view
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
def login_view(request) :
    if request.method=='POST' :
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfull')
            return redirect('/')
    return render(request,'auth/login.html',)

def register_view(request) :
    if request.method=='POST' :
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username,email,password)
        user.save()
    
        return redirect('/login')
    return render(request,'auth/register.html')
    