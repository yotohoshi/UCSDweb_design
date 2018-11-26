from django.http import JsonResponse
from django.shortcuts import render
from Job.models import Job
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.core.paginator import Paginator
from django import template
from overrides import overrides
from .forms import SearchingForm
from Job.models import Job
from User.models import Degree

# Create your views here.

register = template.Library()
AUTH = ['U.S Citizen','Permanent Resident','F-1','H1-B','OPT','CPT','Otherwise Authorized to Work',]
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
            keyword =None

        if self.request.GET.getlist('start_time') != [''] and self.request.GET.getlist('start_time'):
            start_time = self.request.GET.getlist('start_time')[0]
        else:
            start_time = None

        if self.request.GET.getlist('end_time') != [''] and self.request.GET.getlist('end_time'):
            end_time = self.request.GET.getlist('end_time')[0]
        else:
            end_time = None

        if self.request.GET.getlist('degree'):
            degs = self.request.GET.getlist('degree')
        else:
            degs = None

        if self.request.GET.getlist('work_auth'):
            auths = self.request.GET.getlist('work_auth')
        else:
            auths = None

        if self.request.GET.getlist('paid'):
            paid = self.request.GET.getlist('paid')[0]
            if paid == 'True':
                paid = True
            else:
                paid = False
        else:
            paid = None

        if self.request.GET.getlist('job_type'):
            types = self.request.GET.getlist('job_type')
        else:
            types = None

        print(keyword, auths, degs, start_time, end_time, paid, types)

        # store last-searched keyword to account

        if not keyword:
            if auths or degs or start_time or end_time or paid or types:
                keyword = self.request.user.get_keyword()
            else:
                if self.request.GET.getlist('page') and self.request.GET.getlist('page') != 1:
                    keyword = self.request.user.get_keyword()
                else:
                    keyword = ' '
                    self.request.user.save_keyword(keyword)
        else:
            self.request.user.save_keyword(keyword)

        print(keyword, auths, degs, start_time, end_time, paid, types)
        return Job.general_Search(keyword, auths, degs, start_time, end_time, None, paid, types)

    def degrees(self):
        return Degree.objects.all()

    def auths(self):
        return AUTH

    def type(self):
        return JOBTYPE


def add_favorite(request):
    user = request.user.user
    job_id = request.GET.get('job_id', None)
    job_obj = Job.objects.filter(id=job_id)
    data = {
        'success': job_obj.add_to_favorite(user)
    }
    return JsonResponse(data)




'''
def search(request):
    form = SearchForm()
    keyword = form.keyword
'''


