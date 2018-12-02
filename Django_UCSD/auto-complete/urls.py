from django.conf.urls import url
from django.urls import include, path

from Job import views

# app_name = 'Event'
urlpatterns = [

    url(r'^job/test$', views.runTest, name='test'),
    url(r'^job/$', views.JobDefault.as_view(), name='job'),
    url(r'^job&search/$', views.JobSearch.as_view(), name='jobsearch'),
    path('job_add_to_favorite', views.add_to_favorite, name='job_add_to_favorite'),
    path('job_get_favorite_status', views.job_get_favorite_status, name='job_get_favorite_status'),
    path('send_locations', views.send_locations, name='job_send_locations')
]