from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from User.forms import NewUserForm
from Django_UCSD import views
from User.models import User
# Create your views here.


def user_view(request):
    return HttpResponse("Hello")


   # if request.method == 'POST':

       # L_Name = request.POST['L_Name']
       # yr_graduation = request.POST['yr_graduation']
        #major = request.POST['major']
        #degree = request.POST['degree']
        #contact_email = request.POST['contact_email']
        #description = request.POST['description']
        #register_email = request.POST['register_email']
        #password = request.POST['password']


         #   L_Name= L_Name,
         #   yr_graduation = yr_graduation,
         #   major=major,
          #  degree=degree,
           # contact_email=contact_email,
           # description=description,
           # register_email=register_email,
           # password=password,

        # Getters

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        print("OK wor")

        if form.is_valid():
            form.save(commit=True)

            return views.index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'user.html', {'form': form})

def user_view_page(request):
    form = forms.userform()
    return render(request, 'user.html', {'form': form})


def nick_view_page(request):
    nick_context = {'insert_index': "That's good"}
    return render(request, 'nick.html', context=nick_context)


def niupi_view_page(request):
    niupi_context = {'insert_index': "That's good"}
    return render(request, 'niupi.html', context=niupi_context)


def guapi_view_page(request):
    guapi_context = {'insert_index': "That's good"}
    return render(request, 'guapi.html', context=guapi_context)


def pipi_view_page(request):
    pipi_context = {'insert_index': "That's good"}
    return render(request, 'pipi.html', context=pipi_context)


def save(request):
    form = usermodel()
    if form.is_valid():
        form.save(commit=True)
        return user_view_page(request)
    else:
        print('贼你哥，非法输入值！')
    return render(request, 'user.html', {'form': form})
