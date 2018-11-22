from django.shortcuts import render
from Job.models import Job
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.core.paginator import Paginator
from django import template
from overrides import overrides
from .forms import SearchingForm, FilterForm
from Job.models import Job

# Create your views here.

register = template.Library()


class JobDefault(ListView):

    context_object_name = 'jobs'
    template_name = 'jobs_content.html'
    paginate_by = 5

    @overrides
    def get_queryset(self):
        return Job.get_all()


class JobSearch(ListView):

    context_object_name = 'jobs'
    template_name = 'jobs_content.html'
    paginate_by = 5

    @overrides
    def get_queryset(self):
        form = SearchingForm(self.request.GET or None)
        if form.is_valid() and self.request.method == "GET":
            keyword = form.cleaned_data['keyword']
        else:
            keyword = 'google'
            print(form.cleaned_data)

        location = self.request.GET['location']
        start = self.request.GET['start_date']
        paid = self.request.GET['paid']
        BS = self.request.GET['BS']
        print(location, start, paid, BS)

        return Job.general_Search(keyword, None, None, None, None, None, None, None)






'''
def search(request):
    form = SearchForm()
    keyword = form.keyword
'''


