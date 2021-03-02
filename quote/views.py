from django.shortcuts import (
    render, get_object_or_404
)
from .forms import QuoteForm
from .models import Quote


# Create your views here.
def quote(request):
    """ A view to return a users delivery quote and the
    rest of the form to book deliverys """
    scottish_highlands = (
      'AB', 'PA', 'PH', 'FK', 'KA', 'HS', 'IV', 'KW', 'ZE',
    )
    if request.method == 'GET':
        quote_form = QuoteForm()
    if request.method == 'POST':
        total_price = 0
        form_data = {
            'd_postcode': request.POST['d_postcode'].upper(),
            'c_postcode': request.POST['c_postcode'].upper(),
            'height': request.POST['height'],
            'length': request.POST['length'],
            'width': request.POST['width'],
            'weight': request.POST['weight'],
            'd_contact_name': request.POST['d_contact_name'],
            'd_company': request.POST['d_company'],
            'd_email': request.POST['d_email'],
            'd_phone_number': request.POST['d_phone_number'],
            'd_street_address1': request.POST['d_street_address1'],
            'd_street_address2': request.POST['d_street_address2'],
            'd_town_or_city': request.POST['d_town_or_city'],
            'd_county': request.POST['d_county'],
            'c_contact_name': request.POST['c_contact_name'],
            'c_company': request.POST['c_company'],
            'c_email': request.POST['c_email'],
            'c_phone_number': request.POST['c_phone_number'],
            'c_street_address1': request.POST['c_street_address1'],
            'c_street_address2': request.POST['c_street_address2'],
            'c_town_or_city': request.POST['c_town_or_city'],
            'c_county': request.POST['c_county'],
        }
        quote_form = QuoteForm(form_data)

        v_weight = float(form_data['height']) * float(form_data[
          'width']) * float(form_data['length']) / 4000
        a_weight = float(form_data['weight'])

        if form_data['c_postcode'].startswith(("ME15", "TN", )):
            total_price += 0.00
        else:
            total_price += 8.00
        for postcode in scottish_highlands:
            if form_data['d_postcode'].startswith((postcode, )):
                total_price += 10.00

        if v_weight > a_weight:
            if v_weight <= 10:
                total_price += 8.00
            elif v_weight > 10:
                total_price += 8.00
                over_10 = v_weight - 10
                over_10_cost = over_10 * 0.4
                total_price += over_10_cost

        if a_weight > v_weight:
            if a_weight <= 10:
                total_price += 8.00
            elif a_weight > 10:
                total_price += 8.00
                over_10 = a_weight - 10
                over_10_cost = over_10 * 0.4
                total_price += over_10_cost

        context = {
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
