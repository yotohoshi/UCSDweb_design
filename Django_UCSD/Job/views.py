from django.http import JsonResponse
from django.shortcuts import render
from Job.models import Job, Referral
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.core.paginator import Paginator
from django import template
from overrides import overrides
from .forms import SearchingForm
from Job.models import Job, Location
from User.models import Degree, Major
from Company.models import Company

# Create your views here.

register = template.Library()
AUTH = ['U.S Citizen', 'Permanent Resident', 'F-1', 'H1-B', 'OPT', 'CPT', 'Otherwise Authorized to Work']
JOBTYPE = ['Full-time', 'Part-time', 'Contract', 'Temporary', 'Commission', 'Internship', 'Not Available']
DEGS = ['BS', 'BA', 'MS', 'MA', 'PHD', 'MBA', 'NO LIMITED']


class JobDefault(ListView):
    context_object_name = 'jobs'
    template_name = 'jobs_content.html'
    paginate_by = 5

    @overrides
    def get_queryset(self):
        return Job.get_all()

    def degrees(self):
        return Degree.objects.all()

    def auths(self):
        return AUTH

    def type(self):
        return JOBTYPE


class JobSearch(ListView):
    context_object_name = 'jobs'
    template_name = 'jobs_search-result.html'
    paginate_by = 5

    @overrides
    def get_queryset(self):
        form = SearchingForm(self.request.GET or None)
        if form.is_valid() and self.request.method == "GET":
            if form.cleaned_data['keyword']:
                keyword = form.cleaned_data['keyword']
            else:
                keyword = None
        else:
            keyword = None

        if self.request.GET.getlist('degree'):
            degs = self.request.GET.getlist('degree')
        else:
            degs = None

        if self.request.GET.getlist('work_auth'):
            auths = self.request.GET.getlist('work_auth')
        else:
            auths = None

        if self.request.GET.getlist('paid'):
            paid = self.request.GET.getlist('paid')[0] == 'True'
        else:
            paid = None

        if self.request.GET.getlist('job_type'):
            types = self.request.GET.getlist('job_type')
        else:
            types = None

        print(keyword, auths, degs, paid, types)

        # store last-searched keyword to account
        if self.request.user.is_authenticated:
            if not keyword:
                if auths or degs or paid or types:
                    keyword = self.request.user.get_keyword()
                else:
                    if self.request.GET.getlist('page') and self.request.GET.getlist('page') != 1:
                        keyword = self.request.user.get_keyword()
                    else:
                        keyword = ' '
                        self.request.user.save_keyword(keyword)
            else:
                if self.request.user.is_authenticated:
                    self.request.user.save_keyword(keyword)

        print(keyword, auths, degs, paid, types)
        return Job.general_Search(keyword, auths, degs, None, paid, types)

    def degrees(self):
        return Degree.objects.all()

    def auths(self):
        return AUTH

    def type(self):
        return JOBTYPE


def add_to_favorite(request):
    user = request.user.user
    job_id = request.GET.get('job_id', None)
    job_obj = list(Job.objects.filter(id=job_id))[0]
    data = {
        'successful': job_obj.add_to_favorite(user)
    }
    return JsonResponse(data)


def job_get_favorite_status(request):
    user = request.user.user
    job_id = request.GET.get('job_id', None)
    job_obj = list(Job.objects.filter(id=job_id))[0]
    data = {
        'job_status': job_obj.get_favorite_status(user)
    }
    return JsonResponse(data)


'''
def search(request):
    form = SearchForm()
    keyword = form.keyword
'''


def add_referral(request):

    data = {
        'successful': False
    }
    if request.method == 'GET':

        category = []

        if request.GET['position']:
            position = request.GET['position']
            print(position)
        else:
            position = None

        if request.GET.getlist('company'):
            company = request.GET.getlist('company')[0]
        else:
            company = None

        if request.GET.getlist('major'):
            major = request.GET.getlist('major')[0]
        else:
            major = None

        if request.GET.getlist('degree'):
            degree = request.GET.getlist('degree')[0]
        else:
            degree = None

        if request.GET.getlist('location'):
            location = request.GET.getlist('location')[0]
        else:
            location = None

        if request.GET.getlist('S'):
            S = request.GET.getlist('S')[0]
            if S == 'S':
                category.append(S)
        else:
            S = None

        if request.GET.getlist('E'):
            E = request.GET.getlist('E')[0]
            if E == 'E':
                category.append(E)
        else:
            E = None

        if request.GET.getlist('H'):
            H = request.GET.getlist('H')[0]
            if H == 'H':
                category.append(H)
        else:
            H = None

        if request.GET.getlist('EM'):
            EM = request.GET.getlist('EM')[0]
            if EM == 'EM':
                category.append(EM)
        else:
            EM = None

        if request.GET.getlist('A'):
            A = request.GET.getlist('A')[0]
            if A == 'A':
                category.append(A)
        else:
            A = None

        if request.GET.getlist('AR'):
            AR = request.GET.getlist('AR')[0]
            if AR == 'AR':
                category.append(AR)
        else:
            AR = None

        if request.GET.getlist('B'):
            B = request.GET.getlist('B')[0]
            if B == 'B':
                category.append(B)
        else:
            B = None

        if request.GET.getlist('M'):
            M = request.GET.getlist('M')[0]
            if M == 'M':
                category.append(M)
        else:
            M = None

        if request.GET.getlist('AC'):
            AC = request.GET.getlist('AC')[0]
            if AC == 'AC':
                category.append(AC)
        else:
            AC = None

        if request.GET.getlist('PHY'):
            PHY = request.GET.getlist('PHY')[0]
            if PHY == 'PHY':
                category.append(PHY)
        else:
            PHY = None

        if request.GET.getlist('COMM'):
            COMM = request.GET.getlist('COMM')[0]
            if COMM == 'COMM':
                category.append(COMM)
        else:
            COMM = None

        if request.GET.getlist('C'):
            C = request.GET.getlist('C')[0]
            if C == 'C':
                category.append(C)
        else:
            C = None

        if request.GET.getlist('SC'):
            SC = request.GET.getlist('SC')[0]
            if SC == 'SC':
                category.append(SC)
        else:
            SC = None

        if request.GET.getlist('BIO'):
            BIO = request.GET.getlist('BIO')[0]
            if BIO == 'BIO':
                category.append(BIO)
        else:
            BIO = None

        if request.GET.getlist('BE'):
            BE = request.GET.getlist('BE')[0]
            if BE == 'BE':
                category.append(BE)
        else:
            BE = None

        if request.GET.getlist('MUS'):
            MUS = request.GET.getlist('MUS')[0]
            if MUS == 'MUS':
                category.append(MUS)
        else:
            MUS = None

        if request.GET.getlist('CHEM'):
            CHEM = request.GET.getlist('CHEM')[0]
            if CHEM == 'CHEM':
                category.append(CHEM)
        else:
            CHEM = None

        if request.GET.getlist('ELE'):
            ELE = request.GET.getlist('ELE')[0]
            if ELE == 'ELE':
                category.append(ELE)
        else:
            ELE = None

        if request.GET.getlist('BC'):
            BC = request.GET.getlist('BC')[0]
            if BC == 'BC':
                category.append(BC)
        else:
            BC = None

        if request.GET.getlist('L'):
            L = request.GET.getlist('L')[0]
            if L == 'L':
                category.append(L)
        else:
            L = None

        if request.GET.getlist('description'):
            description = request.GET.getlist('description')[0]
        else:
            description = None

        if request.GET.getlist('resume_required'):
            resume_required = request.GET.getlist('resume_required')[0]
            if resume_required == 'on':
                resume_required =True
            else:
                resume_required = False
        else:
            resume_required = None

        if request.GET.getlist('referral_description'):
            referral_description = request.GET.getlist('referral_description')[0]
        else:
            referral_description = None

        provider = request.user.user

        # save the referral with parameters defined above
        success = Referral.save_referral(position, description, major, description, None, None, company, None, category, location,
                               True, provider, referral_description, resume_required)

        if success:
            data = {
                'successful': True
            }
        return JsonResponse(data)
    else:
        return


def fetch_data(request):
    data = {
        'locations': Location.getLocationList(),
        'degrees': Degree.getDegreeList(),
        'majors': Major.getMajorList(),
        'companies': Company.getCompanyList(),
    }
    return JsonResponse(data)
