from django.http import JsonResponse
from django.shortcuts import render
from Event.models import Event
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse, redirect
from overrides import overrides


class event(TemplateView):

    context_object_name = 'events'
    model = Event
    template_name = 'event.html'
    paginate_by = 9
    # template_name = 'event_list.html'
    # all_events = Event.get_all()
    # top5 = Event.get_top_five()
    # paginator = Paginator(all_events, 5)



class EventListView(ListView):

    context_object_name = 'events'
    # model = Event
    template_name = 'event_about.html'
    paginate_by = 7
    def get_queryset(self):
        return Event.get_all()

    def get_all(self):
        return Event.get_all()

    def top5(self):
        return Event.get_top_five()



class EventListViewMonth(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_about.html'

    def get_queryset(self):
        return Event.all_filter_by_month()

    def get_all(self):
        return Event.all_filter_by_month()

    def top5(self):
        return Event.get_top_five()


class EventListViewWeek(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_about.html'

    def get_queryset(self):
        return Event.all_filter_by_week()

    def get_all(self):
        return Event.all_filter_by_week()

    def top5(self):
        return Event.get_top_five()


class EventListViewToday(ListView):
    context_object_name = 'events'
    model = Event
    template_name = 'event_about.html'

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


class List(ListView):
    model = Event
    context_object_name = 'jobs'
    template_name = 'teste.html'

    def get_queryset(self):
        return list(Event.objects.all())[:10]


def add_to_favorite(request):
    user = request.user.user
    event_id = request.GET.get('event_id', None)
    try:
        event_obj = list(Event.objects.filter(id=event_id))[0]
        data = {
            'successful': event_obj.add_to_favorite(user)
        }
    except:
        data = {
            'successful': False
        }
    return JsonResponse(data)


def event_get_favorite_status(request):
    user = request.user.user
    event_id = request.GET.get('event_id', None)
    event_obj = list(Event.objects.filter(id=event_id))[0]
    data = {
        'event_status': event_obj.get_favorite_status(user)
    }
    return JsonResponse(data)


def go_to_event(request):
    user = request.user.user
    event_id = request.GET.get('event_id', None)
    try:
        event_obj = list(Event.objects.filter(id=event_id))[0]
        data = {
            'successful': event_obj.go_to_event(user),
            'go_status': event_obj.get_go_status(user),
            'favorite_status': event_obj.get_favorite_status(user)
        }
    except:
        data = {
            'successful': False
        }
    return JsonResponse(data)


def event_get_go_status(request):
    user = request.user.user
    event_id = request.GET.get('event_id', None)
    event_obj = list(Event.objects.filter(id=event_id))[0]
    data = {
        'event_status': event_obj.get_go_status(user)
    }
    return JsonResponse(data)
