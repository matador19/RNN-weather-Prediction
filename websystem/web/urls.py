from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import changepass,passwordreset  #for class based views

urlpatterns = [
    path("", views.home,name="home"),
    path("login",views.loginform,name="login"),
    path("logout",views.logoutsuccess,name="logout"),
    path("admindashboard",views.admindash,name="admindash"),
    path("supervisordashboard",views.supdash,name="supdash"),
    path("createuser", views.register_request, name="createuser")
]

urlpatterns+=[ 
    path("userlogs",views.userlogs,name="userlogs"),
    path("creationlogs",views.creationlogs,name="creationlogs"),
    path("graphicalreport",views.graphicalreport,name="graphicalreport"),
    path("weatherinput",views.weatherinput,name="weatherinput"),
    path("weatherAPI",views.weatherapi,name="weatherAPI"),
    path("createticket", views.TicketCreation, name="CreateTicket"),
    path("users",views.userslist,name="users"),
    path("users/<int:id>",views.useridentity,name="useridentity"),
    path("deleteuser/<int:id>",views.deleteuser,name="deleteuser"),
    path("powerinputinten",views.checkpowerconsumptioninten,name="powerinputinten"),


    path("passchange/",changepass.as_view(template_name='web/userpass/password-change.html'),name="changepass"),
    path("passsuccess/",views.password_success,name="password_success"),
    path("resetpassword/",passwordreset.as_view(template_name='web/userpass/password-reset-view.html'),name="password_reset"),
    path("resetpassword_sent/",auth_views.PasswordResetDoneView.as_view(template_name='web/userpass/password-reset-done.html'),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='web/userpass/password-reset-confirm.html'),name="password_reset_confirm"),
    path("resetpassowrd_complete/",auth_views.PasswordResetCompleteView.as_view(template_name='web/userpass/password-complete.html'),name="password_reset_complete")
]
