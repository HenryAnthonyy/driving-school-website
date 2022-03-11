from dataclasses import fields
from django import forms
from django.forms import ModelForm, widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email Address'}),
            
        }






class instructorForm(forms.ModelForm):
    class Meta:
        model = instructor
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '@email.com'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            
            
        }


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '@email.com'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            
            
        }

class scheduleForm(forms.ModelForm):
    class Meta:
        model = schedule
        fields = '__all__'

        widgets = {
            'schedule_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'SCHD-'}),
            'schedule_date': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'slots': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Slots'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Price'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Remarks','rows': '2'}),
            'instructor': forms.Select(attrs={'class': 'form-select'}),
        }

class enrollmentForm(forms.ModelForm):
    class Meta:
        model = enrollment
        fields = '__all__'

        widgets = {
            'schedule_code': forms.Select(attrs={'class': 'form-select'}),
            'instructor': forms.Select(attrs={'class': 'form-select'}),
            'student': forms.Select(attrs={'class': 'form-select'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Remarks','rows': '2'}),
        }


class paymentForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = '__all__'

        widgets = {
            'payment_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'REF-'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'REF-', 'type': 'date'}),
            'student': forms.Select(attrs={'class': 'form-select'}),
            'price_paid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Remarks','rows': '2'}),
        }