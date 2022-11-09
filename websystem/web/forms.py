from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from django.forms import FloatField, ModelForm,NumberInput
from web.models import CustomUser,Weatherdata,Ticket,TicketResponse,Threshold

class NewUserForm(UserCreationForm):
    username=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ("username", "email", "first_name","last_name","password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = None
        #Temporary path but prone to SQL injection from the from as the form is not hidden
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget = forms.HiddenInput()
        self.initial['password1'] = User.objects.make_random_password()
        self.initial['password2'] = self.initial['password1']
        


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    

class Customuserform(ModelForm):
    Role=forms.ChoiceField(choices=(('Admin','Admin'),('Supervisor','Supervisor')),required=True,widget=forms.Select(attrs={'class':'form-control'}))
    Phone=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = CustomUser
        fields = ("Role","Phone")

class Weatherinput(ModelForm):
    class Meta:
        model=Weatherdata
        fields=("Temperature",)

        widgets = {
        'Temperature': forms.NumberInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Temperature',
            'min': '-30',
            'max': '60',
            'step': '0.5'
            })
        }

class Changepass(PasswordChangeForm):
    old_password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1=forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2=forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model = User
        fields = ("old_password","new_password1", "new_password2")

class passwordresetform(PasswordResetForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))


class Ticketform(ModelForm):
    class Meta:
        model=Ticket
        fields=('details',)

        widgets = {
        'details': forms.Textarea(attrs={
            'class': "form-control",
            'style': 'max-width: 100rem;',
            'placeholder': 'Enter message here'
            })
        }

class TicketResponseform(ModelForm):
    class Meta:
        model=TicketResponse
        fields=('details',)

        widgets = {
        'details': forms.Textarea(attrs={
            'class': "form-control",
            'style': 'max-width: 100rem;',
            'placeholder': 'Enter message here'
            })
        }

class manualoverrideform(ModelForm):
    class Meta:
        model=Threshold
        fields=("ThresholdkWh",)

        widgets = {
        'ThresholdkWh': forms.NumberInput(attrs={
            'class': "form-control",
            'style': 'max-width: 300px;',
            'placeholder': 'Temperature',
            'min': '0',
            'max': '100',
            'step': '0.001'
            })
        }