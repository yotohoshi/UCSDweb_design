
# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import auth_logout
from .forms import LoginForm
from django.shortcuts import render, redirect
import time
from django.shortcuts import HttpResponseRedirect, HttpResponse, Http404
from Registration.models import Account


def signup(request):
    if request.user.is_authenticated:
        redirect('index')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['password']
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm
    return render(request, 'signup.html', {'form': form})


def UserLogout(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    logout(request)
    return redirect('index')