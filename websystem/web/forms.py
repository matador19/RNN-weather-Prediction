from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from django.forms import FloatField, ModelForm,NumberInput
from web.models import CustomUser,Weatherdata

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class':'form-control'}))
    Role=forms.ChoiceField(choices=(('Admin','Admin'),('Supervisor','Supervisor')),required=True,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name","last_name","Role","password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.Role=self.cleaned_data['Role']
        if commit:
            user.save()
        return user
    

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

