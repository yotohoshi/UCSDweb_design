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
   # print("OK wor")
    if not request.user.is_authenticated:
        return render(request, '404.html')
    form = NewUserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            usr = form.create(request)
            if usr is not None:
                data = {
                    'successful': True,
                    'acc_id': usr.acc.account_id
                }
                usr.acc.set_new_user()
                # TODO Gary Send Request
                return JsonResponse(data)
            else:
                data = {
                    'successful': False,
                    'f_name_err': form['f_name'].errors,
                    'l_name_err': form['l_name'].errors,
                    'yr_grad_err': form['yr_graduation'].errors,
                    'major_err': form['major'].errors,
                    'degree_err':form['degree'].errors,
                    'contact_email_err': form['contact_email'].errors,
                    'alert_err': form.non_field_errors(),
                }
                return JsonResponse(data)
        else:
            data = {
                'successful': False,
                'f_name_err': form['f_name'].errors,
                'l_name_err': form['l_name'].errors,
                'yr_grad_err': form['yr_graduation'].errors,
                'major_err': form['major'].errors,
                'degree_err': form['degree'].errors,
                'contact_email_err': form['contact_email'].errors,
            }
            return JsonResponse(data)
    else:
        return render(request, 'user_creation.html', {'form': form})


def request_all(request):
    data = {
        'majorList': Major.getMajorList(),
        'degreeList': Degree.getDegreeList(),
    }
    return JsonResponse(data)




def profile(request, account_id):
    if request.user.account_id != account_id or not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'profile.html')


class Profile(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'profile_right_lower.html'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return render(self.request, 'REGHTML/not_authorized.html')
        else:
            return list(self.request.user.user.event_set.all())

    def get_majors(self):
        return list(Major.objects.all())

    def get_degrees(self):
        return list(Degree.objects.all())

    def get_favjobs(self):
        if self.request.user.is_authenticated:
            return list(self.request.user.user.job_set.all())
        else:
            return redirect('index')

    def get_referrals(self):
        if self.request.user.is_authenticated:
            return list(self.request.user.user.referral_set.all())
        else:
            return redirect('index')

    '''def get(self, request, account_id):
        if not request.user.is_authenticated:
            return render(request, 'REGHTML/not_authorized.html')
        else:
            return render(request, 'profile_right_lower.html', {'account_id': account_id}, {'majors': Major.objects.all()})'''


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

            if request.POST.getlist('company'):
                company = request.POST.getlist('company')[0]
            else:
                company = None
            print(contact_email, description, degree, yr_graduation, major, company)

            user.update_user_info(major, degree, contact_email, description, yr_graduation, company)
    except:
        data = {'successful': False}

    return JsonResponse(data)
