from asyncio.windows_events import NULL
from datetime import datetime
from statistics import mode
from xmlrpc.client import _datetime_type
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone=models.BigIntegerField(null=True,blank=True)
    Role=models.CharField(max_length=15,choices=[('Admin','Admin'),('Supervisor','Supervisor')])

    def __str__(self):
        return self.user.username


class Logs(models.Model):
    LogId = models.AutoField(primary_key=True)
    CreationDate=models.DateTimeField(default=datetime.now())
    Change=models.TextField()
    Type=models.CharField(max_length=20)
    Initiator=models.ForeignKey(User,on_delete=models.CASCADE,unique=False)

    def __str__(self):
        return self.Change

class Ticket(models.Model):
    TicketId=models.AutoField(primary_key=True)
    CreationDate=models.DateTimeField(default=datetime.now().strftime(("%d.%m.%Y %H:%M:%S")))
    Status=models.BooleanField()
    Initiator=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.TicketId

