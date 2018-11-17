from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth import logout, user_logged_out


def index(request):
    index_page = {'insert_index': "Welcome to UCSD !"}

    return render(request, 'index.html', context=index_page)

