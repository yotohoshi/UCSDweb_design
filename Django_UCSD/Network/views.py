from django.shortcuts import render
from django.views.generic import ListView

from Job.models import Referral
from User.models import User, Request, search_By_Keywords
from django.http import JsonResponse
from User.forms import SearchResultForm


# Create your views here.


def network(request):
    return render(request, 'Network/network.html')


def send_friend_request(request):
    user_id = request.GET.get('user_id', None)
    request_to = User.objects.get(id=user_id)
    if not request_to:
        data = {
            'successful': False
        }
    else:
        data = {
            'successful': request.user.user.send_request(request_to)
        }
    return JsonResponse(data)


def accept_friend_request(request):
    request_id = request.GET.get('request_id', None)
    friend_request = Request.objects.get(id=request_id)
    if not friend_request:
        data = {
            'successful': False
        }
    else:
        data = {
            'successful': request.user.user.accept_request(friend_request)
        }
        return JsonResponse(data)


def deny_friend_request(request):
    request_id = request.GET.get('request_id', None)
    friend_request = Request.objects.get(id=request_id)
    if not friend_request:
        data = {
            'successful': False
        }
    else:
        data = {
            'successful': request.user.user.deny_request(friend_request)
        }
        return JsonResponse(data)


def remove_friend(request):
    user_id = request.GET.get('user_id', None)
    to_remove = User.objects.get(id=user_id)
    if not to_remove:
        data = {
            'successful': False
        }
    else:
        data = {
            'successful': request.user.user.remove_friend(to_remove)
        }
    return JsonResponse(data)


def undo_request(request):
    request_id = request.GET.get('request_id', None)
    friend_request = Request.objects.get(id=request_id)
    if not friend_request:
        data = {
            'successful': False
        }
    else:
        data = {
            'successful': request.user.user.undo_request(friend_request)
        }
    return JsonResponse(data)


def calc_common_friends(request):
    user_id = request.GET.get('request_id', None)
    num = User.get_common_friend_number(request.user.user.id, user_id)
    if num:
        data = {
            'successful': True,
            'num': num,
        }
    else:
        data = {
            'successful': False,
        }
    return JsonResponse(data)


def search(request):
    if request.method == "GET":
        if request.GET.getlist('name'):
            name = request.GET.getlist('name')[0]
        else:
            name = ' '

        if request.user.user.search_result:
            request.user.user.clear_search_results()
        result = search_By_Keywords(name)
        data = {
            'successful': True
        }
        for user in result:
            request.user.user.search_result.add(user)
        return JsonResponse(data)
    else:
        return render(request, '404.html')


class SearchResult(ListView):
    template_name = 'Network/newfriend_search_result.html'
    model = User
    context_object_name = 'results'

    def get_queryset(self):
        return self.request.user.user.search_result.all()


class FriendList(ListView):
    model = User
    context_object_name = 'friends'
    template_name = 'Network/friends_tab.html'

    def get_queryset(self):
        return list(self.request.user.user.friend.all())


class FriendListReferralState(ListView):
    model = User
    context_object_name = 'friends'
    template_name = 'Network/friends_tab_rs.html'

    def get_queryset(self):
        return list(self.request.user.user.friend.all())


class RequestList(ListView):
    model = Request
    context_object_name = 'sent_requests'
    template_name = 'Network/request_tab.html'

    def get_queryset(self):
        return list(self.request.user.user.sent_request.all())

    def get_received_requests(self):
        return list(self.request.user.user.received_request.all())


class RecommendationList(ListView):
    model = User
    context_object_name = 'recommendations'
    template_name = 'Network/recommendation_results.html'

    def get_queryset(self):
        User.set_recommended_list(self.request.user.user)
        return self.request.user.user.get_recommended_user.all()


class ReferralUserList(ListView):
    model = User
    context_object_name = 'referral_users'
    template_name = 'referral_user.html'

    def get_referral_users(self):
        user_id = self.request.GET.getlist('user_id')[0]
        return User.get_referral_users(user_id)


class ReferralList(ListView):
    model = Referral
    context_object_name = 'referrals'
    template_name = 'referrals.html'

    def get_queryset(self):
        user_id = self.request.GET.getlist('user_id')[0]
        user_obj = User.objects.filter(id=user_id)
        return user_obj.referral_set.all()

# This is for demonstration purpose only
