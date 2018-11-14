from django.shortcuts import render

# Create your views here.


from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)


class event(TemplateView):
    template_name = 'events.html'
