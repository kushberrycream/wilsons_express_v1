from django.shortcuts import (
    render, get_object_or_404
)
from .forms import QuoteForm
from .models import Quote


# Create your views here.
def quote(request):
    """ A view to return a users delivery quote and the
    rest of the form to book deliverys """
    SCOT_SURCHARGE = (
        'AB', 'PA', 'PH', 'FK', 'KA', 'HS', 'IV', 'KW', 'ZE',
        'DD', 'DG', 'EH', 'KY', 'ML', 'TD', 'G1', 'G2', 'G3',
        'G4', 'G5', 'G7', 'G8', 'G9',
    )
    LOCAL = (
      'ME15', 'ME17', 'TN1', 'TN2', 'TN3', 'TN4', 'TN5', 'TN9',
    )
    total_price = 0
    v_weight = 0
    a_weight = 0

    if request.method == 'GET':
        quote_form = QuoteForm()
        form_data = None
    if request.method == 'POST':
        if 'service' not in request.POST:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
            }
        elif 'spec_service' not in request.POST:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'service': request.POST['service'],
            }
        else:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'service': request.POST['service'],
                'spec_service': request.POST['spec_service'],
            }

        quote_form = QuoteForm(form_data)

        v_weight = float(form_data['height']) * float(form_data[
            'width']) * float(form_data['length']) / 4000
        a_weight = float(form_data['weight'])
        total_price = 8
        for local in LOCAL:
            if form_data['c_postcode'].startswith((local, )):
                total_price = 0

        for scotland in SCOT_SURCHARGE:
            if form_data['d_postcode'].startswith((scotland, )):
                total_price += 9.00

        if v_weight > a_weight:
            if v_weight <= 1:
                total_price += 4.50
            elif v_weight > 1 and v_weight <= 7:
                total_price += 6.50
            elif v_weight > 7 and v_weight <= 15:
                total_price += 8.50
            elif v_weight > 15:
                total_price += 8.50
                over_10 = v_weight - 10
                over_10_cost = over_10 * 0.4
                total_price += over_10_cost

        if a_weight > v_weight:
            if a_weight <= 1:
                total_price += 4.50
            elif a_weight > 1 and a_weight <= 7:
                total_price += 6.50
            elif a_weight > 7 and a_weight <= 15:
                total_price += 8.50
            elif a_weight > 15:
                total_price += 8.50
                over_10 = a_weight - 10
                over_10_cost = over_10 * 0.4
                total_price += over_10_cost

        if request.POST['service'] == '12am':
            total_price += 9.00
        elif request.POST['service'] == '10am':
            total_price += 13.50

    context = {
        'form_data': form_data,
        'quote_form': quote_form,
        'total_price': total_price,
        'volume': v_weight,
        'weight': a_weight,
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
