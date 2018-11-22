from django.shortcuts import render, redirect
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
            usr.save()
            return redirect('profile')
        else:
            print('ERROR FORM INVALID')
            return render(request, '../templates/registration/user.html', {'form': form})
    else:
        return render(request, '../templates/registration/user.html', {'form': form})


def profile(request):

    return render(request, 'profile.html', )
