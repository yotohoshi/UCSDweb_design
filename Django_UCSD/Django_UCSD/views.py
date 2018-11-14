from django.shortcuts import render


def index(request):
    index_page = {'insert_index': "Welcome to UCSD !"}

    return render(request, 'index.html', context=index_page)