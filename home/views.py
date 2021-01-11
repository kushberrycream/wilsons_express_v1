from django.shortcuts import render


def index(request):
    """ A view to return the index / home page """
    return render(request, 'home/index.html')


def covid(request):
    """ A view to return the covid page """
    return render(request, 'home/covid.html')
