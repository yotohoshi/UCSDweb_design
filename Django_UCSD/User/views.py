from django.shortcuts import render, redirect, Http404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from . import forms
from User.forms import NewUserForm
from Django_UCSD import views
from User.models import User, search_By_Keywords
# Create your views here.


def newuser_page(request):
    index_page = {'insert_index': "Welcome to UCSD !"}

    return render(request, 'profile.html', context=index_page)


def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        print("OK wor")

        if form.is_valid():
            usr = form.save(commit=False)
            usr.acc = request.user
            usr.acc.set_new_user()
            usr.save()
            return redirect('profile', account_id=usr.acc.account_id)
        else:
            print('ERROR FORM INVALID')
            return render(request, '../templates/registration/user.html', {'form': form})
    else:
        return render(request, '../templates/registration/user.html', {'form': form})


def profile(request, account_id):
    if request.user.account_id != account_id:
        return Http404
    return render(request, 'profile.html')
