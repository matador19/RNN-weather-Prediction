from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetConfirmView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from requests import request
from .forms import NewUserForm,Weatherinput, Changepass,passwordresetform,Ticketform,TicketResponseform
from web.models import CustomUser,Logs,Weatherdata,Powerconsumed,Powerconsumeddaily,Ticket,TicketResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json 
from django.views.decorators.csrf import csrf_exempt


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
            createlog=Logs()
            createlog.Change=request.user.username+" created user " + createduser+" as a "+role
            createlog.Type="User creation"
            createlog.Initiator=request.user
            createlog.save()

            return redirect(admindash)
        else:
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
            try:
                #maillog
                template=render_to_string('web/email_template.html',{'name':username})
                mail=EmailMessage(
                    'LOG IN ALERT',
                    template,
                    'xyzpowercompany@gmail.com',
                    [user.email]
                    )
                mail.fail_silently=False
                mail.send()
            except:
                pass
            return redirect(admindash)

        elif user is not None and user.customuser.Role=='Supervisor':
            login(request,user)
            suplog=Logs()
            suplog.Change= username+"  has logged in"
            suplog.Initiator=user
            suplog.Type="LOGIN"
            suplog.save()
            #maillog
            try:
                template=render_to_string('web/email_template.html',{'name':username})
                mail=EmailMessage(
                    'LOG IN ALERT',
                    template,
                    'xyzpowercompany@gmail.com',
                    [user.email]
                    )
                mail.fail_silently=False
                mail.send()
            except:
                pass
            return redirect(supdash)
            
        else:
            # No backend authenticated the credentials
            messages.error(request,("LOGIN CREDENTIALS ARE INCORRECT"))
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
    count_tickets=Ticket.objects.filter(Status=False).count()
    return render(request,'web/admindash.html',context={'count_admin_user':count_admin_user,
                                                        'count_sup_user':count_sup_user,
                                                        'count_tickets':count_tickets})


@login_required
def supdash(request):
    logs=Logs.objects.filter(Initiator=request.user).order_by('-LogId')
    logs=logs[0]
    return render(request,'web/supdash.html',context={'logs':logs})

@login_required
def userlogs(request):
    exclude_list =['User creation','User update','User delete','Password edit']
    logs=Logs.objects.all()
    for item in exclude_list:
        logs=logs.exclude(Type=item).order_by('-LogId') # for all logins to be seen by all admins
    suplogins=Logs.objects.filter(Initiator=request.user).order_by('-LogId')# logins for  specific supervisor
    page = request.GET.get('page', 1)

    # for all logins to be seen by all admins
    paginator = Paginator(logs, 25)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    # logins for  specific supervisor
    suppaginator = Paginator(suplogins, 25)
    try:
        suplogins = suppaginator.page(page)
    except PageNotAnInteger:
        suplogins = suppaginator.page(1)
    except EmptyPage:
        suplogins = suppaginator.page(suppaginator.num_pages)
        
    return render(request,'web/logs.html',context={'users':users,'suplogins':suplogins})

@login_required
def creationlogs(request):
    filtered_items=['LOGIN','LOGOUT']
    logs=Logs.objects.all()
    for item in filtered_items:
        logs=logs.exclude(Type=item).order_by('-LogId')
    print(logs)
    page = request.GET.get('page', 1)
    paginator = Paginator(logs, 25)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,'web/usercreationlogs.html',context={'users':users})


@login_required
def graphicalreport(request):
    return render(request,'web/graphicalreport.html')

@login_required
def weatherinput(request):
    if request.method == 'POST':
        form=Weatherinput(request.POST)
        if form.is_valid():
            Weatherdetails=Weatherdata()
            Weatherdetails.Temperature=form.cleaned_data['Temperature']
            Weatherdetails.Initiator=request.user
            Weatherdetails.save()
            messages.success(request, "Details added successful." )
        else:
            messages.error(request, "Something went wrong.")
    form=Weatherinput()
    Weatherdetails=Weatherdata.objects.all().order_by('-WeatherId')[:10]
    print(Weatherdetails)
    return render(request,'web/weatherinput.html',context={'weatherform':form,'Weatherdetails':Weatherdetails})


def weatherapi(request):
    from datetime import datetime
    fetchdata=Weatherdata.objects.all()
    data={}
    for i in range(fetchdata.count()):
        data[i]={'CreationDate':fetchdata[i].CreationDate.strftime("%d-%m-%Y")}
        data[i]['Temperature']=fetchdata[i].Temperature
    print(data)
    return JsonResponse(data,safe=False)
@login_required
def userslist(request):
    allusers=User.objects.exclude(username=request.user.username)
    return render(request,'web/users.html',context={'users':allusers})
@login_required
def useridentity(request,id):
    useridentity=User.objects.get(pk=id)
    if request.method == "POST":
        form=NewUserForm(request.POST,instance=useridentity)
        if form.is_valid():
            Users=form.save()
            createduser=form.cleaned_data.get('username')
            role=form.cleaned_data.get('Role')
            CustomUser.objects.filter(user=Users).update(Role=role)
            createlog=Logs()
            createlog.Change=request.user.username+" updated user " +useridentity.username+" to "+ createduser+" as a "+role
            createlog.Type="User update"
            createlog.Initiator=request.user
            createlog.save()

            return redirect(admindash)
        else:
            messages.error(request, "Unsuccessful update. Invalid information.")
    form=NewUserForm(instance=useridentity)
    return render(request,'web/userupdate.html',context={'update_form':form})
@login_required
def deleteuser(request,id):
    useridentity=User.objects.get(pk=id)
    User.objects.get(pk=id).delete()
    createlog=Logs()
    createlog.Change=request.user.username+" deleted user " +useridentity.username
    createlog.Type="User deletion"
    createlog.Initiator=request.user
    createlog.save()
    return redirect(admindash)

class changepass(PasswordChangeView):
    form_class=Changepass
    success_url=reverse_lazy('password_success')

def password_success(request):
    createlog=Logs()
    createlog.Change=request.user.username+" changed thier password"
    createlog.Type="Password edit"
    createlog.Initiator=request.user
    createlog.save()
    return render(request,'web/userpass/password-success.html')
    
class passwordreset(PasswordResetView):
    form_class=passwordresetform
    success_url=reverse_lazy('password_reset_done')




@csrf_exempt
def checkpowerconsumptioninten(request):
    def archive():
        values=Powerconsumed.objects.all().last()
        sum=values.kWh
        summed=Powerconsumeddaily()
        summed.kWh=sum
        summed.save()
        Powerconsumed.objects.all().delete()

    powerconsumed=Powerconsumed()
    from datetime import datetime
    now = datetime.now()
    today=now.strftime("%d")
    val={'power consumed':0}
    if request.method=="POST":
        data=request.body
        data=json.loads(data)
        powerconsumed.kWh=data['power consumed']
        powerconsumed.save()
        currentconsumption=Powerconsumed.objects.all().last()
        if currentconsumption!=None:
            latestrecord=currentconsumption.CreationDate.strftime("%d")
            if today != latestrecord:
                archive()

    currentconsumption=Powerconsumed.objects.all().last()
    if currentconsumption!=None:
        latestrecord=currentconsumption.CreationDate.strftime("%d")
        if today == latestrecord:
            vals={}
            val=Powerconsumed.objects.all()
            for i in range(val.count()):
                vals[i]=val[i].kWh
            val=json.loads(json.dumps({'power consumed today':vals}))

        else:
            archive()
    daily_usage=Powerconsumeddaily.objects.all()
    val['power consumed daily']={}
    for x in range(daily_usage.count()):
        dateformat=daily_usage[x].CreationDate.strftime("%m-%d")
        val['power consumed daily'][x]={dateformat:daily_usage[x].kWh}
    #print(val)
    return JsonResponse(val,safe=False)

@login_required
def TicketCreation(request):
    if request.method=="POST": 
        form = Ticketform(request.POST)
        if form.is_valid():
            Ticketcreation=Ticket()
            Ticketcreation.Status=False
            Ticketcreation.details=form.cleaned_data.get('details')
            Ticketcreation.Initiator=request.user
            Ticketcreation.save()
    form=Ticketform()
    ticket=Ticket.objects.filter(Initiator=request.user)[:10]
    #responses=TicketResponse.objects.filter(TicketComment=ticket)
    return render(request=request, template_name="web/Ticketing/CreateTicket.html", context={"form":form,'tickets':ticket})

@login_required
def deleteweather(request,id):
    Weatherdata.objects.get(pk=id).delete()
    createlog=Logs()
    createlog.Change=request.user.username+" deleted a weather entry "
    createlog.Type="Weather deletion"
    createlog.Initiator=request.user
    createlog.save()
    return redirect(weatherinput)
@login_required
def deleteticket(request,id):
    Ticket.objects.get(pk=id).delete()
    return redirect(TicketCreation)

@login_required
def reviewticket(request):
    tickets=Ticket.objects.all()
    return render(request,'web/Ticketing/reviewtickets.html',context={'tickets':tickets})

@login_required
def revieweachticket(request,id):
    tickets=Ticket.objects.get(pk=id)
    if request.method=="POST": 
        form = TicketResponseform(request.POST)
        if form.is_valid():
            response=TicketResponse()
            response.Status=True
            tickets.Status=True
            response.details=form.cleaned_data.get('details')
            response.TicketComment=tickets
            response.Initiator=request.user
            response.save()
    form=TicketResponseform()
    return render(request,'web/Ticketing/revieweachticket.html',context={'ticket':tickets,'form':form})