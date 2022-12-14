from django.contrib import admin
from web.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from web.models import Logs,Weatherdata,Ticket,TicketResponse,Threshold,Powerconsumeddaily,sentmail
# Register your models here.
class AccountInLine(admin.StackedInline):
    model=CustomUser
    can_delete=False
    verbose_name_plural='CustomerUser'

class CustomizedUserAdmin (UserAdmin):
    inlines=(AccountInLine,)

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)

admin.site.register(Logs)
admin.site.register(Weatherdata)
admin.site.register(Ticket)
admin.site.register(TicketResponse)
admin.site.register(Threshold)
admin.site.register(Powerconsumeddaily)
admin.site.register(sentmail)