from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.core.validators import validate_email
from .models import Account


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    # log in check and throwing exceptions
    def login(self, request):
        if self.is_valid():
            email = self.cleaned_data['email']
            raw_password = self.cleaned_data['password']
            if not Account.objects.filter(email=email):
                self.add_error(None, "you have not been registered yet.")
            user = authenticate(email=email, password=raw_password)
            if user is not None:
                login(request, user)
                return True
            else:
                if Account.objects.filter(email=email):
                    self.add_error('password', "Invalid Password.")
                    return False


class SignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirmed_password = forms.CharField(widget=forms.PasswordInput())

    # log in check and throwing exceptions
    def signup(self, request):
        if self.is_valid():
            email = self.cleaned_data['email']
            raw_password = self.cleaned_data['password']
            confirm_password = self.cleaned_data['confirmed_password']
            if Account.objects.filter(email=email):
                self.add_error(None, "this email address has already been registered.")
                return False
            if raw_password != confirm_password:
                self.add_error('confirmed_password', "confirm password is not the same")
            else:
                return True


