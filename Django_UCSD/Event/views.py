from django.shortcuts import render
from Event.models import Event
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)


class event(TemplateView):
    template_name = 'events.html'


class EventListView(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
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
    template_name = 'event_list.html'

    def get_queryset(self):
        return Event.all_filter_by_month()

    def top5(self):
        return Event.get_top_five()


class EventListViewWeek(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
        return Event.all_filter_by_week()

    def top5(self):
        return Event.get_top_five()


class EventListViewToday(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
        return Event.all_filter_by_today()

    def top5(self):
        return Event.get_top_five()


class EventDetailView(DetailView):
    context_object_name = 'event_detail'
    model = Event
    # template_name = "event_list.html"
