from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm
from web.models import CustomUser,Logs
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    return render(request,'web/welcome.html')

   
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            User=form.save()
            createduser=form.cleaned_data.get('username')
            role=form.cleaned_data.get('Role')
            CustomUser.objects.create(
                user=User,
                Role=role
            )
            messages.success(request, "Registration successful." )
            createlog=Logs()
            createlog.Change=request.user.username+" created user " + createduser+" as a "+role
            createlog.Type="User creation"
            createlog.Initiator=request.user
            createlog.save()

            return redirect(admindash)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="web/createuser.html", context={"register_form":form})
    

def loginform(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None and user.customuser.Role=='Admin':
            # A backend authenticated the credentials
            login(request,user)
            #logs
            adminlog=Logs()
            adminlog.Change= username+"  has logged in"
            adminlog.Initiator=user
            adminlog.Type="LOGIN"
            adminlog.save()
            #maillog
            template=render_to_string('web/email_template.html',{'name':username})
            mail=EmailMessage(
                'LOG IN ALERT',
                template,
                'aleki1313@proton.me',
                [user.email]
                )
            mail.fail_silently=False
            mail.send()
            return redirect(admindash)

        elif user is not None and user.customuser.Role=='Supervisor':
            login(request,user)
            suplog=Logs()
            suplog.Change= username+"  has logged in"
            suplog.Initiator=user
            suplog.Type="LOGIN"
            suplog.save()
            return redirect(supdash)
            
        else:
            # No backend authenticated the credentials
            messages.success(request,("LOGIN CREDENTIALS ARE INCORRECT"))
            return redirect(loginform)
        
    else:
         return render(request,'web/login.html')

def logoutsuccess(request):
    logoutlog=Logs()
    user=request.user
    logoutlog.Change= user.username+"  has logout"
    logoutlog.Initiator= user
    logoutlog.Type="LOGOUT"
    logoutlog.save()
    logout(request)
    return redirect(home)

@login_required
def admindash(request):
    count_admin_user=User.objects.filter(customuser__Role="Admin").count()
    count_sup_user=User.objects.filter(customuser__Role="Supervisor").count()
    
    return render(request,'web/admindash.html',context={'count_admin_user':count_admin_user,
                                                        'count_sup_user':count_sup_user})

@login_required
def supdash(request):
    return render(request,'web/supdash.html')

@login_required
def userlogs(request):
    logs=Logs.objects.exclude(Type='User creation').order_by('-LogId')
    page = request.GET.get('page', 1)
    paginator = Paginator(logs, 25)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,'web/logs.html',context={'users':users})