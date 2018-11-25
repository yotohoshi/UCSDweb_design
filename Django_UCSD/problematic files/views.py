from django.shortcuts import render, redirect, Http404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from . import forms
from django.views.generic import ListView
from User.forms import NewUserForm
from User.models import Degree,Major,Event
from Django_UCSD import views
from User.models import User, search_By_Keywords
# Create your views here.


def newuser_page(request):
    index_page = {'insert_index': "Welcome to UCSD !"}

    return render(request, 'profile.html', context=index_page)


def users(request):
    if not request.user.is_authenticated:
        return Http404

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




class Profile(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'profile_right_lower.html'

    def get_queryset(self):
        return list(self.request.user.user.favorite_event.all())

    def get_majors(self):
        return list(Major.objects.all())

    def get_degrees(self):
        return list(Degree.objects.all())

    def get_favjobs(self):
        return list()


def edit_profile(request):

    user = request.user.user
    if request.method == 'POST':

        if request.POST.getlist('contact_email'):
            contact_email = request.POST.getlist('contact_email')[0]
            user.contact_email = contact_email
            user.save()

        else:
            contact_email = None

        if request.POST.getlist('yr_graduation'):
            yr_graduation = request.POST.getlist('yr_graduation')[0]
            user.yr_graduation = yr_graduation
            user.save()

        if request.POST.getlist('degree'):
            degree = request.POST.getlist('degree')[0]

    return redirect('profile', account_id=request.user.account_id)
