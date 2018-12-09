from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('list', views.List.as_view(), name='list'),
    path('', views.network, name='network'),
    path('friends', views.FriendList.as_view(), name='friends'),
    path('request', views.RequestList.as_view(), name='request'),
    path('remove_friend', views.remove_friend, name='remove_friend'),
    path('search_friend', views.search, name='search_friend'),
    path('search_result', views.SearchResult.as_view(), name='search_result'),
    path('send_request', views.send_friend_request, name='send_request'),
    path('accept_request', views.accept_friend_request, name='accept_request'),
    path('deny_request', views.deny_friend_request, name='deny_request'),
    path('undo_request', views.undo_request, name='undo_request'),
    path('calc_common_friends', views.calc_common_friends, name='calc_common_friends'),
    path('recommendations', views.RecommendationList.as_view(), name='recommendations'),
]
