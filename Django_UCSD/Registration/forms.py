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
                self.add_error(None, "Please Register an Account.")
                return None
            user = authenticate(email=email, password=raw_password)
            if user is not None:
                login(request, user)
                return user
            else:
                if Account.objects.filter(email=email):
                    self.add_error('password', "Invalid Password.")
                    return None


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
                self.add_error('email', "Email address has been registered.")
                return False
            if raw_password != confirm_password:
                self.add_error('confirmed_password', "Confirm password is not the same")
            else:
                return True

    def save(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        usr = Account.objects.create_user(email, password)
        return usr


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirmed_password = forms.CharField(widget=forms.PasswordInput())

    def changepassword(self, request):
        if self.is_valid():
            old_password = self.cleaned_data['old_password']
            new_password = self.cleaned_data['new_password']
            confirmed_password = self.cleaned_data['confirmed_password']
            email = request.user.email
            user = authenticate(email=email, password=old_password)
            print(email, old_password)
            if user is not None:
                if new_password == confirmed_password:
                    user.set_password(new_password)
                    user.save()
                    return True
                else:
                    self.add_error('confirmed_password', "confirm password is not the same")
                    return False
            else:
                self.add_error('old_password', "Incorrect password")
                return False

