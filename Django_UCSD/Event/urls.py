from django.conf.urls import url
from django.urls import include, path

from Event import views

# app_name = 'Event'
urlpatterns = [

    url(r'^event$', views.event.as_view(), name='event'),
    # url(r'^event_list$', views.EventListView.as_view(), name='event_list'),
    # url(r'^event_list_5$', views.EventListViewTop5.as_view(), name='event_list_top5'),
    url(r'^event_list&filter=month$', views.EventListViewMonth.as_view(), name='event_list_month'),
    url(r'^event_list&filter=week$', views.EventListViewWeek.as_view(), name='event_list_week'),
    url(r'^event_list&filter=today$', views.EventListViewToday.as_view(), name='event_list_today'),
]
