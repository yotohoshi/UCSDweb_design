from django.conf.urls import url
from django.urls import include, path

from Job import views

# app_name = 'Event'
urlpatterns = [

    url(r'^job$', views.JobDefault.as_view(), name='job'),
    url(r'^job&search$', views.JobSearch.as_view(), name='jobsearch'),
]