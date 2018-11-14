from django.conf.urls import url
from django.urls import include, path
from Registration import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('Registration/templates/', views.signup, name='signup'),
]
