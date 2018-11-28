from django.conf.urls import url
from django.urls import include, path
from django.views.generic import TemplateView

from Event import views

# app_name = 'Event'
urlpatterns = [

    # url(r'^events/$', views.event.as_view(), name='event'),
    url(r'^events/$', views.EventListView.as_view(), name='event'),
    # url(r'^event_list_5$', views.EventListViewTop5.as_view(), name='event_list_top5'),
    url(r'^event_list&filter=month$', views.EventListViewMonth.as_view(), name='event_list_month'),
    url(r'^event_list&filter=week$', views.EventListViewWeek.as_view(), name='event_list_week'),
    url(r'^event_list&filter=today$', views.EventListViewToday.as_view(), name='event_list_today'),
    # path('templates/event_content.html', TemplateView.as_view(template_name='event_content.html')),
    # path('templates/event_description.html', TemplateView.as_view(template_name='event_description.html')),
    path('test', views.List.as_view(), name='test'),
    path('event_add_to_favorite', views.add_to_favorite, name='event_add_to_favorite'),
    path('event_get_favorite_status', views.event_get_favorite_status, name='event_get_favorite_status'),
]
