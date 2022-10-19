from asyncio.windows_events import NULL
from datetime import datetime
from statistics import mode
from unittest.util import _MAX_LENGTH
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
    CreationDate=models.DateTimeField(auto_now_add=True)
    Change=models.TextField()
    Type=models.CharField(max_length=20)
    Initiator=models.ForeignKey(User,on_delete=models.CASCADE,unique=False)

    def __str__(self):
        return self.Change

class Ticket(models.Model):
    TicketId=models.AutoField(primary_key=True)
    CreationDate=models.DateTimeField(auto_now_add=True)
    Status=models.BooleanField()
    details=models.CharField(max_length=100)
    Initiator=models.ForeignKey(User,on_delete=models.CASCADE,unique=False)

    def __str__(self):
        return str(self.TicketId)

class Weatherdata(models.Model):
    WeatherId=models.AutoField(primary_key=True)
    CreationDate=models.DateTimeField(auto_now_add=True)
    Temperature=models.FloatField()
    Initiator=models.ForeignKey(User,on_delete=models.CASCADE,unique=False)

    def __str__(self):
        return str(self.WeatherId)

class Powerconsumed(models.Model):
    PowerConsumeId=models.AutoField(primary_key=True)
    CreationDate=models.DateTimeField(auto_now_add=True)
    kWh=models.FloatField()

    def __str__(self):
        return str(self.PowerConsumeId)

class Powerconsumeddaily(models.Model):
    PowerConsumeddailyId=models.AutoField(primary_key=True)
    CreationDate=models.DateTimeField(auto_now_add=True)
    kWh=models.FloatField()

    def __str__(self):
        return str(self.PowerConsumeId)

class TicketResponse(models.Model):
    TicketResponseId=models.AutoField(primary_key=True)
    CreationDate=models.DateTimeField(auto_now_add=True)
    Status=models.BooleanField()
    details=models.CharField(max_length=100)
    TicketComment=models.ForeignKey(Ticket,on_delete=models.CASCADE,unique=False)
    Initiator=models.ForeignKey(User,on_delete=models.CASCADE,unique=False)

    def __str__(self):
        return str(self.TicketResponseId)