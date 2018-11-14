
from django.urls import include, path

from Event import views

urlpatterns = [

    path('Event/templates/', views.event.as_view(), name='event'),
]
