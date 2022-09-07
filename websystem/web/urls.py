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
