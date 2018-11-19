from django.conf.urls import url
from django.urls import include, path
from Registration import views
from django.contrib.auth import logout


urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),

    url(r'^account/signin$', views.UserLogin, name='userlogin'),
    url(r'^account/logout/$', views.UserLogout, name='userlogout'),
    url(r'^account/signup/$', views.UserSignup, name='usersignup'),
]
