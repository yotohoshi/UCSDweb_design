# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import auth_logout
from .forms import LoginForm, SignupForm
from django import forms
from django.shortcuts import render, redirect
import time
from django.shortcuts import HttpResponseRedirect, HttpResponse, Http404
from Registration.models import Account


def UserSignup(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = SignupForm(request.POST)
    if request.method == 'POST':
        if form.signup(request):
            redirect('userlogin')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm
        return render(request, 'signup.html', {'form': form})




def UserLogin(request):
    if request.user.is_authenticated:
        redirect('index')
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.login(request):
            redirect('index')
        else:
            return render(request, 'redirect_sign_in.html', {'form': form})
    else:
        form = LoginForm
        return render(request, 'redirect_sign_in.html', {'form': form})


def UserLogout(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    logout(request)
    return redirect('index')
