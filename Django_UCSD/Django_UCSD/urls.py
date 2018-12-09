"""Django_UCSD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('', include('Event.urls')),
    path('', include('Registration.urls')),
    path('', include('Job.urls')),
    path('usr/', include('User.urls')),
    path('network/', include('Network.urls')),
    path('templates/banner.html', TemplateView.as_view(template_name='banner.html')),
    path('templates/index_top_right.html', TemplateView.as_view(template_name='index_top_right.html')),
    path('templates/searchbar.html', TemplateView.as_view(template_name='searchbar.html')),
    path('templates/sidebar.html', TemplateView.as_view(template_name='sidebar.html')),
    path('templates/simple_keyword_search.html', TemplateView.as_view(template_name='simple_keyword_search.html')),
    path('templates/personal_links.html', TemplateView.as_view(template_name='personal_links.html')),
    path('templates/profile_right_upper.html', TemplateView.as_view(template_name='profile_right_upper.html')),
    path('templates/event_content.html', TemplateView.as_view(template_name='event_content.html')),
    path('templates/event_description.html', TemplateView.as_view(template_name='event_description.html')),
    path('templates/jobs_content.html', TemplateView.as_view(template_name='jobs_content.html')),
    path('templates/profile_right_lower.html', TemplateView.as_view(template_name='profile_right_lower.html')),
    path('templates/calendar.html', TemplateView.as_view(template_name='calendar.html')),
    path('templates/add_referral.html', TemplateView.as_view(template_name='add_referral.html')),
    path('event_about', TemplateView.as_view(template_name='event_about.html')),
    path('view_referral', TemplateView.as_view(template_name='view_referral.html')),
    path('templates/referrals.html', TemplateView.as_view(template_name='referrals.html')),
    path('view_referral', TemplateView.as_view(template_name='view_referral.html'), name = 'view_referral'),
    path('templates/signin_integrated.html', TemplateView.as_view(template_name='signin_integrated.html')),
    path('templates/logout_successful.html', TemplateView.as_view(template_name='logout_successful.html')),
    path('templates/signin_successful.html', TemplateView.as_view(template_name='signin_successful.html')),
    path('templates/signup_successful.html', TemplateView.as_view(template_name='signup_successful.html')),
    path('404', TemplateView.as_view(template_name='404.html')),
    path('templates/user_creation.html', TemplateView.as_view(template_name='user_creation.html')),
    path('templates/Network/newfriend_search_result.html', TemplateView.as_view(template_name='Network/newfriend_search_result.html')),
    path('templates/Network/recommendation_results.html', TemplateView.as_view(template_name='Network/recommendation_results.html')),
    path('templates/Network/friends_tab.html', TemplateView.as_view(template_name='Network/friends_tab.html')),
    path('templates/Network/request_tab.html', TemplateView.as_view(template_name='Network/request_tab.html')),
    path('templates/simple_keyword_search1.html', TemplateView.as_view(template_name='simple_keyword_search1.html')),
    path('templates/error_popup.html', TemplateView.as_view(template_name='error_popup.html')),
]
