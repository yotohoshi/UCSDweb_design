# Create your views here.
import warnings

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import auth_logout
from django.template.response import TemplateResponse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .forms import LoginForm, SignupForm, ChangePasswordForm
from django import forms
from django.shortcuts import render, redirect, resolve_url
import time
from django.shortcuts import HttpResponseRedirect, HttpResponse, Http404
from Registration.models import Account
from django.urls import reverse


def UserSignup(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = SignupForm(request.POST)
    if request.method == 'POST':
        if form.signup(request):
            form.save()
            return redirect('new_user')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm
        return render(request, 'signup.html', {'form': form})


def UserLogin(request):
    # if request.user.is_authenticated:
        # return redirect('index')
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.login(request):
            return redirect('index')
        else:
            return render(request, 'redirect_sign_in.html', {'form': form})
    else:
        form = LoginForm
        return render(request, 'redirect_sign_in.html', {'form': form})


def UserLogout(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    logout(request)
    return redirect('index')


def PasswordRetrievalEmail(request):
    if request.user.is_authenticated:
        return redirect('index')


def ChangePassword(request):
    if not request.user.is_authenticated:
        logout(request)
        return redirect('userlogin')
    form = ChangePasswordForm(request.POST)
    if request.method == 'POST':
        if form.changepassword(request):
            logout(request)
            return redirect('userlogin')
        else:
            return render(request, 'change_password.html', {'form': form})
    else:
        form = ChangePasswordForm
        return render(request, 'change_password.html', {'form': form})


# 抄的
# 4 views for password reset:
# - password_reset sends the mail
# - password_reset_done shows a success message for the above
# - password_reset_confirm checks the link the user clicked and
#   prompts for a new password
# - password_reset_complete shows a success message for the above

@csrf_protect
def password_reset(request, is_admin_site=False,
                   template_name='REGHTML/password_reset_form.html',
                   email_template_name='REGHTML/password_reset_email.html',
                   subject_template_name='REGHTML/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   current_app=None,
                   extra_context=None,
                   html_email_template_name=None):
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
            }

            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': ('Password reset'),
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


def password_reset_done(request,
                        template_name='REGHTML/password_reset_done.html',
                        current_app=None, extra_context=None):
    context = {
        'title': ('Password reset sent')
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


# Doesn't need csrf_protect since no-one can guess the URL
@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='REGHTML/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           current_app=None, extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = Account
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = ('Enter new password')
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = ('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


def password_reset_complete(request,
                            template_name='REGHTML/password_reset_complete.html',
                            current_app=None, extra_context=None):
    context = {
        'login_url': '/account/signin ',
        'title': ('Password reset complete')
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)
