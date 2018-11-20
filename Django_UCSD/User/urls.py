from django.conf.urls import url
from django.views.generic import TemplateView

from User import views
from django.urls import path

urlpatterns = [
   # url(r'^$', views.user_view, name='user_view'),
   # url(r'^profile/', views.user_view_page, name='form_name'),
    url(r'^$', views.users, name='users'),
    path('', views.newuser_page, name='newuser_page'),
    #url(r'^user/create/$', 'User.views.create_user'),
    url(r'^profile/', views.profile, name='profile'),
    path('profile/templates/sidebar.html', TemplateView.as_view(template_name='sidebar.html')),
    path('profile/templates/simple_keyword_search.html', TemplateView.as_view(template_name='simple_keyword_search.html')),
    path('profile/templates/personal_links.html', TemplateView.as_view(template_name='personal_links.html')),
    path('profile/templates/profile_right_upper.html', TemplateView.as_view(template_name='profile_right_upper.html')),
    path('profile/templates/profile_right_lower_about.html', TemplateView.as_view(template_name='profile_right_lower_about.html')),
    path('profile/templates/profile_right_lower_events.html', TemplateView.as_view(template_name='profile_right_lower_events.html')),
]