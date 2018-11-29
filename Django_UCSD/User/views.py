from django.shortcuts import render, redirect, Http404, HttpResponseRedirect
from django.core.serializers.json import Deserializer
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from . import forms
from django.views.generic import ListView
from User.forms import NewUserForm
from django.views.generic import ListView
from User.models import User, search_By_Keywords, Major, Degree
from Event.models import Event
# from django.utils import simplejson


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


def profile(request, account_id):
    if request.user.account_id != account_id:
        return Http404
    return render(request, 'profile.html')


class Profile(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'profile_right_lower.html'

    def get_queryset(self):
        return list(self.request.user.user.event_set.all())

    def get_majors(self):
        return list(Major.objects.all())

    def get_degrees(self):
        return list(Degree.objects.all())

    def get_favjobs(self):
        return list(self.request.user.user.job_set.all())


def edit_profile(request):
    data = {'successful': True}
    user = request.user.user
    try:
        if request.method == 'POST':
            # print(request.POST.get('contact_email'))
            # new_data = simplejson.loads(request.POST.get('contact_email'))
            # new_data = Deserializer(request.POST['contact_email'])
            if request.POST.getlist('contact_email'):
                contact_email = request.POST.getlist('contact_email')[0]
            else:
                contact_email = None

            if request.POST.getlist('yr_graduation'):
                yr_graduation = request.POST.getlist('yr_graduation')[0]
            else:
                yr_graduation = None

            if request.POST.getlist('degree'):
                degree = request.POST.getlist('degree')[0]
            else:
                degree = None

            if request.POST.getlist('major'):
                major = request.POST.getlist('major')[0]
            else:
                major = None

            if request.POST.getlist('description'):
                description = request.POST.getlist('description')[0]
            else:
                description = None
            print(contact_email, description, degree, yr_graduation, major)

            user.update_user_info(major, degree, contact_email, description, yr_graduation)
    except:
        data = {'successful': False}

    return JsonResponse(data)
