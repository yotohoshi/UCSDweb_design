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
    path('templates/footnote_circles.html', TemplateView.as_view(template_name='footnote_circles.html')),
    path('templates/banner.html', TemplateView.as_view(template_name='banner.html')),
    path('templates/login.html', TemplateView.as_view(template_name='login.html')),
    path('templates/index_top_right.html', TemplateView.as_view(template_name='index_top_right.html')),
    path('templates/searchbar.html', TemplateView.as_view(template_name='searchbar.html')),
    path('templates/sidebar.html', TemplateView.as_view(template_name='sidebar.html')),
    path('templates/simple_keyword_search.html', TemplateView.as_view(template_name='simple_keyword_search.html')),
    path('templates/personal_links.html', TemplateView.as_view(template_name='personal_links.html')),
    path('templates/profile_right_upper.html', TemplateView.as_view(template_name='profile_right_upper.html')),
   # path('templates/profile_right_lower.html', TemplateView.as_view(template_name='profile_right_lower_about.html')),

    path('templates/profile_right_lower_events.html', TemplateView.as_view(template_name='profile_right_lower_events.html')),
    path('templates/event_content.html', TemplateView.as_view(template_name='event_content.html')),
    path('templates/event_description.html', TemplateView.as_view(template_name='event_description.html')),
    # path('templates/adfilter.html', TemplateView.as_view(template_name='adfilter.html')),
    path('templates/jobs_content.html', TemplateView.as_view(template_name='jobs_content.html')),
    path('templates/profile_right_lower.html', TemplateView.as_view(template_name='profile_right_lower.html')),
    path('templates/calendar.html', TemplateView.as_view(template_name='calendar.html')),
    path('event_about', TemplateView.as_view(template_name='event_about.html')),

]
