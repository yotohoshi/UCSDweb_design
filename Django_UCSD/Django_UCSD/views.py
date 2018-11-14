from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)


def index(request):
    index_page = {'insert_index': "Welcome to UCSD !"}

    return render(request, 'index.html', context=index_page)
