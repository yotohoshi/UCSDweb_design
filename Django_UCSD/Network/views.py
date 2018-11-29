from django.shortcuts import render
from django.views.generic import ListView
from User.models import User, Request, search_By_Keywords
from django.http import JsonResponse
from User.forms import SearchResultForm
# Create your views here.


class BackgroundWithFriendList(ListView):
    template_name = 'Social_base.html'
    model = User
    context_object_name = 'friends'

    def get_queryset(self):
        return self.request.user.user.get_friends()

    def get_requests(self):
        return self.request.user.user.get_requests()


def send_friend_request(request):
    user_id = request.GET.get('user_id', None)
    request_to = User.objects.filter(id=user_id)
    data = {
        'success': request.user.user.send_request(request_to)
    }
    return JsonResponse(data)


def accept_friend_request(request):
    request_id = request.GET.get('request_id', None)
    friend_request = Request.objects.filter(id=request_id)
    data = {
        'success': request.user.user.accept_request(friend_request)
    }
    return JsonResponse(data)


def deny_friend_request(request):
    request_id = request.GET.get('request_id', None)
    friend_request = Request.objects.filter(id=request_id)
    data = {
        'success': request.user.user.deny_request(friend_request)
    }
    return JsonResponse(data)


def remove_friend(request):
    user_id = request.GET.get('user_id', None)
    to_remove = User.objects.filter(id=user_id)
    data = {
        'success': request.user.user.remove_friend(to_remove)
    }
    return JsonResponse(data)


class SearchResult(ListView):
    template_name = 'social_search_result.html'
    model = User
    context_object_name = 'results'

    def get_queryset(self):

        form = SearchResultForm(self.request.GET or None)
        if form.is_valid() and self.request.method == "GET":
            if form.cleaned_data['name']:
                name = form.cleaned_data['name']
            else:
                name = ' '
        else:
            name = ' '

        # debug
        print(name)

        result = search_By_Keywords(name)
        return result


class List(ListView):
    template_name = 'friend_recommandation.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()
