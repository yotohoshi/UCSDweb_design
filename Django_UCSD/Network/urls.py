from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('list', views.List.as_view(), name='list'),
]