from django.shortcuts import render
from Event.models import Event
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)


class event(TemplateView):
    template_name = 'events.html'


class EventListView(ListView):
    model = Event

    def get_queryset(self):
        return Event.get_all()
