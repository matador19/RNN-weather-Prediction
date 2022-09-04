from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="dashboard"),
    path("login",views.loginform,name="login"),
    path("admindashboard",views.admindash,name="admindash"),
    path("supervisordashboard",views.supdash,name="supdash")
]
