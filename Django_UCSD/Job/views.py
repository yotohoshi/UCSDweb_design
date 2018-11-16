from django.shortcuts import render
from Job.models import Job
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.core.paginator import Paginator


# Create your views here.


class job(ListView):

    context_object_name = 'jobs'
    template_name = 'jobs.html'
    paginate_by = 5

    def get_queryset(self):
        return Job.objects.all()
