from django.conf.urls import url
from django.views.generic import TemplateView

from User import views
from django.urls import path

urlpatterns = [
   # url(r'^$', views.user_view, name='user_view'),
   # url(r'^profile/', views.user_view_page, name='form_name'),
    url(r'^user_creation/', views.users, name='new_user'),
    # path('', views.newuser_page, name='newuser_page'),
    # url(r'^user/create/$', 'User.views.create_user'),
    url(r'^profile/', views.profile, name='profile'),
]
