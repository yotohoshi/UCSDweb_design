from django.shortcuts import render
from Event.models import Event
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse, redirect
from overrides import overrides


class event(ListView):

    context_object_name = 'events'
    model = Event
    template_name = 'event_content.html'
    paginate_by = 5
    # template_name = 'event_list.html'
    # all_events = Event.get_all()
    # top5 = Event.get_top_five()
    # paginator = Paginator(all_events, 5)


    def get_queryset(self):
        return Event.get_all()

    def get_all(self):
        return Event.get_all()

    def top5(self):
        return Event.get_top_five()

    def by_month(self, request):
        return Event.all_filter_by_month()

    def by_week(self):
        return Event.all_filter_by_week()

    def by_today(self):
        return Event.all_filter_by_today()



class EventListViewMonth(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_content.html'

    def get_queryset(self):
        return Event.all_filter_by_month()

    def get_all(self):
        return Event.all_filter_by_month()

    def top5(self):
        return Event.get_top_five()


class EventListViewWeek(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_content.html'

    def get_queryset(self):
        return Event.all_filter_by_week()

    def get_all(self):
        return Event.all_filter_by_week()

    def top5(self):
        return Event.get_top_five()


class EventListViewToday(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_content.html'

    def get_queryset(self):
        return Event.all_filter_by_today()

    def get_all(self):
        return Event.all_filter_by_today()

    def top5(self):
        return Event.get_top_five()


class EventDetailView(DetailView):
    context_object_name = 'event_detail'
    model = Event
    # template_name = "event_list.html"
