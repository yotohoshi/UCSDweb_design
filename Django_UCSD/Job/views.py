from django.shortcuts import render
from Job.models import Job
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.core.paginator import Paginator
from django import template
from overrides import overrides
from Job.forms import SearchForm
from Job.models import Job

# Create your views here.

register = template.Library()


class JobDefault(ListView):

    context_object_name = 'jobs'
    template_name = 'jobs.html'
    paginate_by = 5

    @overrides
    def get_queryset(self):
        return Job.get_all()


class JobSearch(ListView):

    context_object_name = 'jobs'
    template_name = 'jobs.html'
    paginate_by = 5

    @overrides
    def get_queryset(self):
        form = SearchForm(self.request.GET or None)
        if form.is_valid() and self.request.method == "GET":
            keyword = form.cleaned_data['keyword']
        else:
            keyword = ''

        return Job.search_By_Keywords(keyword)






'''
def search(request):
    form = SearchForm()
    keyword = form.keyword
'''


