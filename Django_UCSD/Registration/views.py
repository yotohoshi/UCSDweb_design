
# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import auth_logout
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from Registration.models import Account


def signup(request):
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
    logout(request)
    return redirect('index')
