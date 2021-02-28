from django.shortcuts import (
    render
)
from quote.forms import QuoteForm


def index(request):
    """ A view to return the index / home page """
    if request.method == 'GET':
        quote_form = QuoteForm()
    if request.method == 'POST':
        form_data = {
            'delivery': request.POST['delivery'].upper(),
            'collection': request.POST['collection'].upper(),
        }
        quote_form = QuoteForm(form_data)
        total_price = 0
        if "ME15" in form_data[
          'collection'] or "TN" in form_data['collection']:
            total_price = 0
        else:
            total_price = 10

        context = {
            'quote_form': quote_form,
            'total_price': total_price,
        }
        return render(request, 'quote/quote.html', context)

    context = {'quote_form': quote_form, }

    return render(request, 'home/index.html', context)


def covid(request):
    """ A view to return the covid page """
    return render(request, 'home/covid.html')
