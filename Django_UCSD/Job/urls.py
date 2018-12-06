from django.conf.urls import url
from django.urls import include, path

from Job import views

# app_name = 'Event'
urlpatterns = [

    url(r'^job/$', views.JobDefault.as_view(), name='job'),
    url(r'^job&search/$', views.JobSearch.as_view(), name='jobsearch'),
    path('job_add_to_favorite', views.add_to_favorite, name='job_add_to_favorite'),
    path('job_get_favorite_status', views.job_get_favorite_status, name='job_get_favorite_status'),
    path('job_fetch_data', views.fetch_data ,name='job_fetch_data'),
    path('add_referral', views.add_referral, name='add_referral'),
    path('referral_list', views.Referrals.as_view(), name='referral_list'),
    path('toggle_referral_activate', views.toggle_activate_referral, name='toggle_referral_activate'),
]