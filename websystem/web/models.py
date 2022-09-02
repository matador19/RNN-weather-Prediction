from asyncio.windows_events import NULL
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone=models.BigIntegerField(null=True,blank=True)
    Role=models.CharField(max_length=15,choices=[('Admin','Admin'),('Supervisor','Supervisor')])

    def __str__(self):
        return self.user.username
