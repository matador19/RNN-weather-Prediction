from django.urls import path
from . import views

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
    path("weatherinput",views.weatherinput,name="weatherinput")
]
