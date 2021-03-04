from django.shortcuts import (
  render
)
from quote.forms import QuoteForm


def index(request):
    """ A view to return the index / home page """
    if request.method == 'GET':
        quote_form = QuoteForm()

    context = {'quote_form': quote_form, }

    return render(request, 'home/index.html', context)


def covid(request):
    """ A view to return the covid page """
    return render(request, 'home/covid.html')
