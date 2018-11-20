from django.conf.urls import url
from django.urls import include, path
from Registration import views
from django.contrib.auth import logout


urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),

    url(r'^account/signin$', views.UserLogin, name='userlogin'),
    url(r'^account/logout/$', views.UserLogout, name='userlogout'),
    url(r'^account/signup/$', views.UserSignup, name='usersignup'),
    url(r'^account/changepassword/$', views.ChangePassword, name='changepassword'),
    url(r'^account/password_reset/$', views.password_reset, name='password_reset'),
    url(r'^account/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^account/password_reset_done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^account/password_reset_confirm/$', views.password_reset_complete, name='password_reset_complete'),

]
