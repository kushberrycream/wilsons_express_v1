from django.shortcuts import (
    render, get_object_or_404
)
from .forms import QuoteForm
from .models import Quote


# Create your views here.
def quote(request):
    """ A view to return a users delivery quote and the
    rest of the form to book deliverys """
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


def partial_quote(request, quote_id):
    """ A view to return a users delivery quote and the
    rest of the form to book deliverys """

    quote = get_object_or_404(Quote, pk=quote_id)
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST, instance=quote)
    context = {
        'quote_form': quote_form,

    }

    return render(request, 'quote/quote.html', context)
