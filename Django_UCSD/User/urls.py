from django.conf.urls import url
from User import views


urlpatterns = [
   # url(r'^$', views.user_view, name='user_view'),
   # url(r'^profile/', views.user_view_page, name='form_name'),
    url(r'^$', views.users, name='users'),
    url(r'^nick', views.nick_view_page, name='nick'),
    url(r'^niupi', views.niupi_view_page, name='niupi'),
    url(r'^guapi', views.guapi_view_page, name='guapi'),
    url(r'^pipi', views.pipi_view_page, name='pipi'),
    #url(r'^user/create/$', 'User.views.create_user')
]