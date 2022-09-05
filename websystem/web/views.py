from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'web/welcome.html')

   

def loginform(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None and user.customuser.Role=='Admin':
            # A backend authenticated the credentials
            login(request,user)
            return redirect(admindash)

        elif user is not None and user.customuser.Role=='Supervisor':
            login(request,user)
            return redirect(supdash)
            
        else:
            # No backend authenticated the credentials
            messages.success(request,("LOGIN CREDENTIALS ARE INCORRECT"))
            return redirect(loginform)
        
    else:
         return render(request,'web/login.html')

def logoutsuccess(request):
    logout(request)
    return redirect(home)

@login_required
def admindash(request):
    return render(request,'web/admindash.html')

@login_required
def supdash(request):
    return render(request,'web/supdash.html')

