from django.conf.urls import url
from django.urls import include, path

from Job import views

# app_name = 'Event'
urlpatterns = [

    url(r'^job$', views.job.as_view(), name='job'),
]