from django.shortcuts import (
    render
)
from quote.forms import QuoteForm


def index(request):
    """ A view to return the index / home page """
    scottish_highlands = (
      'AB', 'PA', 'PH', 'FK', 'KA', 'HS', 'IV', 'KW', 'ZE',
      )
    if request.method == 'GET':
        quote_form = QuoteForm()
    if request.method == 'POST':
        total_price = 0.00
        form_data = {
            'd_postcode': request.POST['d_postcode'].upper(),
            'c_postcode': request.POST['c_postcode'].upper(),
            'height': request.POST['height'],
            'length': request.POST['length'],
            'width': request.POST['width'],
            'weight': request.POST['weight'],
        }

        quote_form = QuoteForm(form_data)

        v_weight = float(form_data['height']) * float(form_data[
          'width']) * float(form_data['length']) / 4000
        a_weight = float(form_data['weight'])

        if form_data['c_postcode'].startswith(("ME15", "TN", )):
            total_price += 0.00
        else:
            total_price += 8.00
        for x in scottish_highlands:
            if form_data['d_postcode'].startswith((x, )):
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

    context = {'quote_form': quote_form, }

    return render(request, 'home/index.html', context)


def covid(request):
    """ A view to return the covid page """
    return render(request, 'home/covid.html')
