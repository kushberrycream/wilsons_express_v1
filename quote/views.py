from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from measurement.measures import Weight
from .forms import QuoteForm, BookingForm
from .models import Quote, Bookings
from decimal import Decimal


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
    total_price = Decimal(0)
    v_weight = Decimal(0)
    a_weight = Decimal(0)
    if request.method == 'GET':
        quote_form = QuoteForm()
        form_data = None
    if request.method == 'POST':
        items = 0
        if 'service' not in request.POST:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
            }
        elif 'spec_service' not in request.POST:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'service': request.POST['service'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
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
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
            }
        quote = Quote()
        quote_form = QuoteForm(form_data, instance=quote)
        if quote_form.is_valid():
            quote.volume_weight1 = 0
            quote.volume_weight2 = 0
            quote.volume_weight3 = 0
            quote.volume_weight4 = 0
            a_weight1 = 0
            a_weight2 = 0
            a_weight3 = 0
            a_weight4 = 0

            # Item 1
            v_weight = float(form_data['height']) * float(form_data[
                'width']) * float(form_data['length']) / 5000
            a_weight = float(form_data['weight'])
            items += 1
            quote.volume_weight = Weight(kg=v_weight)

            # Item 2
            if 'weight1' in request.POST:
                v_weight1 = float(form_data['height1']) * float(form_data[
                    'width1']) * float(form_data['length1']) / 5000
                a_weight1 = float(form_data['weight1'])
                quote.volume_weight1 = Weight(kg=v_weight1)
                if v_weight1 != 0:
                    items += 1

            # Item 3
            if 'weight2' in request.POST:
                v_weight2 = float(form_data['height2']) * float(form_data[
                    'width2']) * float(form_data['length2']) / 5000
                a_weight2 = float(form_data['weight2'])
                quote.volume_weight2 = Weight(kg=v_weight2)
                if v_weight2 != 0:
                    items += 1

            # Item 4
            if 'weight3' in request.POST:
                v_weight3 = float(form_data['height3']) * float(form_data[
                    'width3']) * float(form_data['length3']) / 5000
                a_weight3 = float(form_data['weight3'])
                quote.volume_weight3 = Weight(kg=v_weight3)
                if v_weight3 != 0:
                    items += 1

            # Item 5
            if 'weight4' in request.POST:
                v_weight4 = float(form_data['height4']) * float(form_data[
                    'width4']) * float(form_data['length4']) / 5000
                a_weight4 = float(form_data['weight4'])
                quote.volume_weight4 = Weight(kg=v_weight4)
                if v_weight4 != 0:
                    items += 1

            overall_weight = Decimal(
              a_weight + a_weight1 + a_weight2 + a_weight3 + a_weight4
            )

            overall_volume = Decimal(
              v_weight + v_weight1 + v_weight2 + v_weight3 + v_weight4
            )

            quote.overall_volume = Weight(kg=overall_volume)
            quote.overall_weight = Weight(kg=overall_weight)
            quote.items = items

            total_price = Decimal(8)
            # Checks if postcode is a local one
            for local in LOCAL:
                if form_data['c_postcode'].startswith((local, )):
                    total_price = Decimal(0)

                if form_data['d_postcode'].startswith((local, )):
                    total_price -= Decimal(3)

            # checks if postcode is a scottish postcode
            for scotland in SCOT_SURCHARGE:
                if form_data['d_postcode'].startswith((scotland, )):
                    total_price += Decimal(9.00)

            # checks if overall volume is heavier than overall weight
            if overall_volume > overall_weight:
                if overall_volume <= 1:
                    total_price += Decimal(4.50)
                elif overall_volume > 1 and overall_volume <= 7:
                    total_price += Decimal(6.50)
                elif overall_volume > 7 and overall_volume <= 15:
                    total_price += Decimal(8.50)
                elif overall_volume > 15:
                    total_price += Decimal(8.50)
                    over_10 = overall_volume - 10
                    over_10_cost = Decimal(over_10) * Decimal(0.4)
                    total_price += Decimal(over_10_cost)

            # checks if overall weight is heavier than overall volume
            if overall_weight > overall_volume:
                if overall_weight <= 1:
                    total_price += Decimal(4.50)
                elif overall_weight > 1 and overall_weight <= 7:
                    total_price += Decimal(6.50)
                elif overall_weight > 7 and overall_weight <= 15:
                    total_price += Decimal(8.50)
                elif overall_weight > 15:
                    total_price += Decimal(8.50)
                    over_10 = overall_weight - 10
                    over_10_cost = Decimal(over_10) * Decimal(0.4)
                    total_price += Decimal(over_10_cost)

            # checks which service is chosen
            if 'service' in request.POST:
                if request.POST['service'] == '12am':
                    total_price += Decimal(9.00)
                elif request.POST['service'] == '10am':
                    total_price += Decimal(13.50)
                elif request.POST['service'] == "null":
                    total_price += Decimal(0)

            # checks if a special service is selected
            if 'spec_service' in request.POST:
                if request.POST['spec_service'] == 'Fragile' or request.POST[
                        'spec_service'] == 'Liquid':
                    total_price += Decimal(0.75)
                elif request.POST['spec_service'] == 'Security':
                    total_price += Decimal(1.50)
                elif request.POST['spec_service'] == 'Live Fish':
                    total_price += Decimal(16.50)

            # Check for non-conveyable and excess parcel sizes
            height = Decimal(request.POST['height'])
            length = Decimal(request.POST['length'])
            width = Decimal(request.POST['width'])
            height1 = Decimal(request.POST['height1'])
            length1 = Decimal(request.POST['length1'])
            width1 = Decimal(request.POST['width1'])
            height2 = Decimal(request.POST['height2'])
            length2 = Decimal(request.POST['length2'])
            width2 = Decimal(request.POST['width2'])
            height3 = Decimal(request.POST['height3'])
            length3 = Decimal(request.POST['length3'])
            width3 = Decimal(request.POST['width3'])
            height4 = Decimal(request.POST['height4'])
            length4 = Decimal(request.POST['length4'])
            width4 = Decimal(request.POST['width4'])

            if (
                    height > Decimal(60) and
                    length > Decimal(60) and
                    width > Decimal(60) or
                    height1 > Decimal(60) and
                    length1 > Decimal(60) and
                    width1 > Decimal(60) or
                    height2 > Decimal(60) and
                    length2 > Decimal(60) and
                    width2 > Decimal(60) or
                    height3 > Decimal(60) and
                    length3 > Decimal(60) and
                    width3 > Decimal(60) or
                    height4 > Decimal(60) and
                    length4 > Decimal(60) and
                    width4 > Decimal(60)):
                total_price += Decimal(4.00)

            if (
                    height >= Decimal(120) and
                    length >= Decimal(55) and
                    width >= Decimal(50) or
                    height1 >= Decimal(120) and
                    length1 >= Decimal(55) and
                    width1 >= Decimal(50) or
                    height2 >= Decimal(120) and
                    length2 >= Decimal(55) and
                    width2 >= Decimal(50) or
                    height3 >= Decimal(120) and
                    length3 >= Decimal(55) and
                    width3 >= Decimal(50) or
                    height4 >= Decimal(120) and
                    length4 >= Decimal(55) and
                    width4 >= Decimal(50)):
                total_price += Decimal(4.00)

            if (
                    height >= Decimal(120) and
                    length >= Decimal(50) and
                    width >= Decimal(55) or
                    height1 >= Decimal(120) and
                    length1 >= Decimal(50) and
                    width1 >= Decimal(55) or
                    height2 >= Decimal(120) and
                    length2 >= Decimal(50) and
                    width2 >= Decimal(55) or
                    height3 >= Decimal(120) and
                    length3 >= Decimal(50) and
                    width3 >= Decimal(55) or
                    height4 >= Decimal(120) and
                    length4 >= Decimal(50) and
                    width4 >= Decimal(55)):
                total_price += Decimal(4.00)

            if (
                    height >= Decimal(55) and
                    length >= Decimal(120) and
                    width >= Decimal(50) or
                    height1 >= Decimal(55) and
                    length1 >= Decimal(120) and
                    width1 >= Decimal(50) or
                    height2 >= Decimal(55) and
                    length2 >= Decimal(120) and
                    width2 >= Decimal(50) or
                    height3 >= Decimal(55) and
                    length3 >= Decimal(120) and
                    width3 >= Decimal(50) or
                    height4 >= Decimal(55) and
                    length4 >= Decimal(120) and
                    width4 >= Decimal(50)):
                total_price += Decimal(4.00)

            if (
                    (height >= Decimal(55) and
                     length >= Decimal(50) and
                     width >= Decimal(120)) or
                    (height1 >= Decimal(55) and
                     length1 >= Decimal(50) and
                     width1 >= Decimal(120)) or
                    (height2 >= Decimal(55) and
                     length2 >= Decimal(50) and
                     width2 >= Decimal(120)) or
                    (height3 >= Decimal(55) and
                     length3 >= Decimal(50) and
                     width3 >= Decimal(120)) or
                    (height4 >= Decimal(55) and
                     length4 >= Decimal(50) and
                     width4 >= Decimal(120))):
                total_price += Decimal(4.00)
            if (
                    (height >= Decimal(50) and
                     length >= Decimal(120) and
                     width >= Decimal(55)) or
                    (height1 >= Decimal(50) and
                     length1 >= Decimal(120) and
                     width1 >= Decimal(55)) or
                    (height2 >= Decimal(50) and
                     length2 >= Decimal(120) and
                     width2 >= Decimal(55)) or
                    (height3 >= Decimal(50) and
                     length3 >= Decimal(120) and
                     width3 >= Decimal(55)) or
                    (height4 >= Decimal(50) and
                     length4 >= Decimal(120) and
                     width4 >= Decimal(55))):
                total_price += Decimal(4.00)
            if (
                    (height >= Decimal(50) and
                     length >= Decimal(55) and
                     width >= Decimal(120)) or
                    (height1 >= Decimal(50) and
                     length1 >= Decimal(55) and
                     width1 >= Decimal(120)) or
                    (height2 >= Decimal(50) and
                     length2 >= Decimal(55) and
                     width2 >= Decimal(120)) or
                    (height3 >= Decimal(50) and
                     length3 >= Decimal(55) and
                     width3 >= Decimal(120)) or
                    (height4 >= Decimal(50) and
                     length4 >= Decimal(55) and
                     width4 >= Decimal(120))):
                total_price += Decimal(4.00)

            if (
                    (height >= Decimal(160) and
                     length + width >= Decimal(120)) or
                    (height1 >= Decimal(160) and
                     length1 + width1 >= Decimal(120)) or
                    (height2 >= Decimal(160) and
                     length2 + width2 >= Decimal(120)) or
                    (height3 >= Decimal(160) and
                     length3 + width3 >= Decimal(120)) or
                    (height4 >= Decimal(160) and
                     length4 + width4 >= Decimal(120))):
                total_price += Decimal(8.00)

            if (
                    (length >= Decimal(160) and
                     height + width >= Decimal(120)) or
                    (length2 >= Decimal(160) and
                     height2 + width2 >= Decimal(120)) or
                    (length3 >= Decimal(160) and
                     height3 + width3 >= Decimal(120)) or
                    (length4 >= Decimal(160) and
                     height4 + width4 >= Decimal(120)) or
                    (length1 >= Decimal(160) and
                     height1 + width1 >= Decimal(120))):
                total_price += Decimal(8.00)

            if (
                    (width >= Decimal(160) and
                     height + length >= Decimal(120)) or
                    (width1 >= Decimal(160) and
                     height1 + length1 >= Decimal(120)) or
                    (width2 >= Decimal(160) and
                     height2 + length2 >= Decimal(120)) or
                    (width3 >= Decimal(160) and
                     height3 + length3 >= Decimal(120)) or
                    (width >= Decimal(160) and
                     height4 + length4 >= Decimal(120))):
                total_price += Decimal(8.00)

            if total_price < 5:
                total_price = Decimal(5)

            quote = Quote()
            quote = quote_form.save()
            quote.quote = total_price
            quote.volume_weight = v_weight
            quote.save()
            if 'details' in request.POST:
                booking_form = BookingForm(form_data)

                context = {
                    'form_data': form_data,
                    'booking_form': booking_form,
                    'quote_form': quote_form,
                    'total_price': total_price,
                }
                if quote_form.is_valid():
                    quote_form.save()
                return render(request, 'quote/details.html', context)
            else:
                return redirect(
                  reverse('partial_quote', args=[quote.quote_ref]))

    context = {
        'form_data': form_data,
        'quote_form': quote_form,
        'total_price': total_price,
        'volume': v_weight,
        'weight': a_weight,
    }

    return render(request, 'quote/quote.html', context)


def partial_quote(request, quote_ref):
    SCOT_SURCHARGE = (
        'AB', 'PA', 'PH', 'FK', 'KA', 'HS', 'IV', 'KW', 'ZE',
        'DD', 'DG', 'EH', 'KY', 'ML', 'TD', 'G1', 'G2', 'G3',
        'G4', 'G5', 'G7', 'G8', 'G9',
    )
    LOCAL = (
        'ME15', 'ME17', 'TN1', 'TN2', 'TN3', 'TN4', 'TN5', 'TN9',
    )
    total_price = Decimal(0)

    if request.method == 'GET':
        quote = get_object_or_404(Quote, quote_ref=quote_ref)
        quote_form = QuoteForm(instance=quote)
    if request.method == 'POST':
        items = 0
        if 'service' not in request.POST:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
            }
        elif 'spec_service' not in request.POST:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'service': request.POST['service'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
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
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
            }
        quote = get_object_or_404(Quote, quote_ref=quote_ref)
        quote_form = QuoteForm(form_data, instance=quote)
        if quote_form.is_valid():
            total_price = Decimal(0)
            quote.volume_weight1 = 0
            quote.volume_weight2 = 0
            quote.volume_weight3 = 0
            quote.volume_weight4 = 0
            a_weight1 = 0
            a_weight2 = 0
            a_weight3 = 0
            a_weight4 = 0

            # Item 1
            v_weight = float(form_data['height']) * float(form_data[
                'width']) * float(form_data['length']) / 5000
            a_weight = float(form_data['weight'])
            items += 1
            quote.volume_weight = Weight(kg=v_weight)

            # Item 2
            if 'weight1' in request.POST:
                v_weight1 = float(form_data['height1']) * float(form_data[
                    'width1']) * float(form_data['length1']) / 5000
                a_weight1 = float(form_data['weight1'])
                quote.volume_weight1 = Weight(kg=v_weight1)
                if v_weight1 != 0:
                    items += 1

            # Item 3
            if 'weight2' in request.POST:
                v_weight2 = float(form_data['height2']) * float(form_data[
                    'width2']) * float(form_data['length2']) / 5000
                a_weight2 = float(form_data['weight2'])
                quote.volume_weight2 = Weight(kg=v_weight2)
                if v_weight2 != 0:
                    items += 1

            # Item 4
            if 'weight3' in request.POST:
                v_weight3 = float(form_data['height3']) * float(form_data[
                    'width3']) * float(form_data['length3']) / 5000
                a_weight3 = float(form_data['weight3'])
                quote.volume_weight3 = Weight(kg=v_weight3)
                if v_weight3 != 0:
                    items += 1

            # Item 5
            if 'weight4' in request.POST:
                v_weight4 = float(form_data['height4']) * float(form_data[
                    'width4']) * float(form_data['length4']) / 5000
                a_weight4 = float(form_data['weight4'])
                quote.volume_weight4 = Weight(kg=v_weight4)
                if v_weight4 != 0:
                    items += 1

            overall_weight = (
              a_weight + a_weight1 + a_weight2 + a_weight3 + a_weight4
            )

            overall_volume = (
              v_weight + v_weight1 + v_weight2 + v_weight3 + v_weight4
            )

            quote.overall_volume = Weight(kg=overall_volume)
            quote.overall_weight = Weight(kg=overall_weight)
            quote.items = items

            total_price = Decimal(8)
            for local in LOCAL:
                if form_data['c_postcode'].startswith((local, )):
                    total_price = Decimal(0)

                if form_data['d_postcode'].startswith((local, )):
                    total_price -= Decimal(3)

            # checks if postcode is a scottish postcode
            for scotland in SCOT_SURCHARGE:
                if form_data['d_postcode'].startswith((scotland, )):
                    total_price += Decimal(9.00)

            # checks if overall volume is heavier than overall weight
            if overall_volume > overall_weight:
                if overall_volume <= 1:
                    total_price += Decimal(4.50)
                elif overall_volume > 1 and overall_volume <= 7:
                    total_price += Decimal(6.50)
                elif overall_volume > 7 and overall_volume <= 15:
                    total_price += Decimal(8.50)
                elif overall_volume > 15:
                    total_price += Decimal(8.50)
                    over_10 = overall_volume - 10
                    over_10_cost = Decimal(over_10) * Decimal(0.4)
                    total_price += Decimal(over_10_cost)

            # checks if overall weight is heavier than overall volume
            if overall_weight > overall_volume:
                if overall_weight <= 1:
                    total_price += Decimal(4.50)
                elif overall_weight > 1 and overall_weight <= 7:
                    total_price += Decimal(6.50)
                elif overall_weight > 7 and overall_weight <= 15:
                    total_price += Decimal(8.50)
                elif overall_weight > 15:
                    total_price += Decimal(8.50)
                    over_10 = overall_weight - 10
                    over_10_cost = Decimal(over_10) * Decimal(0.4)
                    total_price += Decimal(over_10_cost)

            # checks which service is chosen
            if 'service' in request.POST:
                if request.POST['service'] == '12am':
                    total_price += Decimal(9.00)
                elif request.POST['service'] == '10am':
                    total_price += Decimal(13.50)
                elif request.POST['service'] == "null":
                    total_price += Decimal(0)

            # checks if a special service is selected
            if 'spec_service' in request.POST:
                if request.POST['spec_service'] == 'Fragile' or request.POST[
                        'spec_service'] == 'Liquid':
                    total_price += Decimal(0.75)
                elif request.POST['spec_service'] == 'Security':
                    total_price += Decimal(1.50)
                elif request.POST['spec_service'] == 'Live Fish':
                    total_price += Decimal(16.50)

            # Check for non-conveyable and excess parcel sizes
            height = Decimal(request.POST['height'])
            length = Decimal(request.POST['length'])
            width = Decimal(request.POST['width'])
            height1 = Decimal(request.POST['height1'])
            length1 = Decimal(request.POST['length1'])
            width1 = Decimal(request.POST['width1'])
            height2 = Decimal(request.POST['height2'])
            length2 = Decimal(request.POST['length2'])
            width2 = Decimal(request.POST['width2'])
            height3 = Decimal(request.POST['height3'])
            length3 = Decimal(request.POST['length3'])
            width3 = Decimal(request.POST['width3'])
            height4 = Decimal(request.POST['height4'])
            length4 = Decimal(request.POST['length4'])
            width4 = Decimal(request.POST['width4'])

            if (
                    height > Decimal(60) and
                    length > Decimal(60) and
                    width > Decimal(60) or
                    height1 > Decimal(60) and
                    length1 > Decimal(60) and
                    width1 > Decimal(60) or
                    height2 > Decimal(60) and
                    length2 > Decimal(60) and
                    width2 > Decimal(60) or
                    height3 > Decimal(60) and
                    length3 > Decimal(60) and
                    width3 > Decimal(60) or
                    height4 > Decimal(60) and
                    length4 > Decimal(60) and
                    width4 > Decimal(60)):
                total_price += Decimal(4.00)

            if (
                    height >= Decimal(120) and
                    length >= Decimal(55) and
                    width >= Decimal(50) or
                    height1 >= Decimal(120) and
                    length1 >= Decimal(55) and
                    width1 >= Decimal(50) or
                    height2 >= Decimal(120) and
                    length2 >= Decimal(55) and
                    width2 >= Decimal(50) or
                    height3 >= Decimal(120) and
                    length3 >= Decimal(55) and
                    width3 >= Decimal(50) or
                    height4 >= Decimal(120) and
                    length4 >= Decimal(55) and
                    width4 >= Decimal(50)):
                total_price += Decimal(4.00)

            if (
                    height >= Decimal(120) and
                    length >= Decimal(50) and
                    width >= Decimal(55) or
                    height1 >= Decimal(120) and
                    length1 >= Decimal(50) and
                    width1 >= Decimal(55) or
                    height2 >= Decimal(120) and
                    length2 >= Decimal(50) and
                    width2 >= Decimal(55) or
                    height3 >= Decimal(120) and
                    length3 >= Decimal(50) and
                    width3 >= Decimal(55) or
                    height4 >= Decimal(120) and
                    length4 >= Decimal(50) and
                    width4 >= Decimal(55)):
                total_price += Decimal(4.00)

            if (
                    height >= Decimal(55) and
                    length >= Decimal(120) and
                    width >= Decimal(50) or
                    height1 >= Decimal(55) and
                    length1 >= Decimal(120) and
                    width1 >= Decimal(50) or
                    height2 >= Decimal(55) and
                    length2 >= Decimal(120) and
                    width2 >= Decimal(50) or
                    height3 >= Decimal(55) and
                    length3 >= Decimal(120) and
                    width3 >= Decimal(50) or
                    height4 >= Decimal(55) and
                    length4 >= Decimal(120) and
                    width4 >= Decimal(50)):
                total_price += Decimal(4.00)

            if (
                    (height >= Decimal(55) and
                     length >= Decimal(50) and
                     width >= Decimal(120)) or
                    (height1 >= Decimal(55) and
                     length1 >= Decimal(50) and
                     width1 >= Decimal(120)) or
                    (height2 >= Decimal(55) and
                     length2 >= Decimal(50) and
                     width2 >= Decimal(120)) or
                    (height3 >= Decimal(55) and
                     length3 >= Decimal(50) and
                     width3 >= Decimal(120)) or
                    (height4 >= Decimal(55) and
                     length4 >= Decimal(50) and
                     width4 >= Decimal(120))):
                total_price += Decimal(4.00)
            if (
                    (height >= Decimal(50) and
                     length >= Decimal(120) and
                     width >= Decimal(55)) or
                    (height1 >= Decimal(50) and
                     length1 >= Decimal(120) and
                     width1 >= Decimal(55)) or
                    (height2 >= Decimal(50) and
                     length2 >= Decimal(120) and
                     width2 >= Decimal(55)) or
                    (height3 >= Decimal(50) and
                     length3 >= Decimal(120) and
                     width3 >= Decimal(55)) or
                    (height4 >= Decimal(50) and
                     length4 >= Decimal(120) and
                     width4 >= Decimal(55))):
                total_price += Decimal(4.00)
            if (
                    (height >= Decimal(50) and
                     length >= Decimal(55) and
                     width >= Decimal(120)) or
                    (height1 >= Decimal(50) and
                     length1 >= Decimal(55) and
                     width1 >= Decimal(120)) or
                    (height2 >= Decimal(50) and
                     length2 >= Decimal(55) and
                     width2 >= Decimal(120)) or
                    (height3 >= Decimal(50) and
                     length3 >= Decimal(55) and
                     width3 >= Decimal(120)) or
                    (height4 >= Decimal(50) and
                     length4 >= Decimal(55) and
                     width4 >= Decimal(120))):
                total_price += Decimal(4.00)

            if (
                    (height >= Decimal(160) and
                     length + width >= Decimal(120)) or
                    (height1 >= Decimal(160) and
                     length1 + width1 >= Decimal(120)) or
                    (height2 >= Decimal(160) and
                     length2 + width2 >= Decimal(120)) or
                    (height3 >= Decimal(160) and
                     length3 + width3 >= Decimal(120)) or
                    (height4 >= Decimal(160) and
                     length4 + width4 >= Decimal(120))):
                total_price += Decimal(8.00)

            if (
                    (length >= Decimal(160) and
                     height + width >= Decimal(120)) or
                    (length2 >= Decimal(160) and
                     height2 + width2 >= Decimal(120)) or
                    (length3 >= Decimal(160) and
                     height3 + width3 >= Decimal(120)) or
                    (length4 >= Decimal(160) and
                     height4 + width4 >= Decimal(120)) or
                    (length1 >= Decimal(160) and
                     height1 + width1 >= Decimal(120))):
                total_price += Decimal(8.00)

            if (
                    (width >= Decimal(160) and
                     height + length >= Decimal(120)) or
                    (width1 >= Decimal(160) and
                     height1 + length1 >= Decimal(120)) or
                    (width2 >= Decimal(160) and
                     height2 + length2 >= Decimal(120)) or
                    (width3 >= Decimal(160) and
                     height3 + length3 >= Decimal(120)) or
                    (width >= Decimal(160) and
                     height4 + length4 >= Decimal(120))):
                total_price += Decimal(8.00)

            if total_price < 5:
                total_price = Decimal(5)

            quote.quote = total_price
            quote = quote_form.save()
            if 'details' in request.POST:
                context = {
                    'quote': quote,
                    'quote_form': quote_form,
                    'total_price': total_price,
                }
                if quote_form.is_valid():
                    quote_form.save()

                return redirect(reverse(
                  'details', args=[quote.quote_ref]))

    context = {
        'quote': quote,
        'quote_form': quote_form,
        'total_price': total_price,

    }

    return render(request, 'quote/quote.html', context)


def delivery_details(request, quote_ref):
    """ A view to return a users delivery price and the
    rest of the form to book deliveries """
    if request.method == 'GET':
        quote = get_object_or_404(Quote, quote_ref=quote_ref)
        booking_form = BookingForm(instance=quote)
    if request.method == 'POST':
        quote = get_object_or_404(Quote, quote_ref=quote_ref)
        if 'service' not in request.POST:
            form_data = {
                'd_contact_name': request.POST['d_contact_name'],
                'd_company': request.POST['d_company'],
                'd_email': request.POST['d_email'],
                'd_phone_number': request.POST['d_phone_number'],
                'd_street_address1': request.POST['d_street_address1'],
                'd_street_address2': request.POST['d_street_address2'],
                'd_town_or_city': request.POST['d_town_or_city'],
                'd_county': request.POST['d_county'],
                'd_postcode': quote.d_postcode,
                'c_contact_name': request.POST['c_contact_name'],
                'c_company': request.POST['c_company'],
                'c_email': request.POST['c_email'],
                'c_phone_number': request.POST['c_phone_number'],
                'c_street_address1': request.POST['c_street_address1'],
                'c_street_address2': request.POST['c_street_address2'],
                'c_town_or_city': request.POST['c_town_or_city'],
                'c_county': request.POST['c_county'],
                'c_postcode': quote.c_postcode,
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
            }
        elif 'spec_service' not in request.POST:
            form_data = {
                'd_contact_name': request.POST['d_contact_name'],
                'd_company': request.POST['d_company'],
                'd_email': request.POST['d_email'],
                'd_phone_number': request.POST['d_phone_number'],
                'd_street_address1': request.POST['d_street_address1'],
                'd_street_address2': request.POST['d_street_address2'],
                'd_town_or_city': request.POST['d_town_or_city'],
                'd_county': request.POST['d_county'],
                'd_postcode': quote.d_postcode,
                'c_contact_name': request.POST['c_contact_name'],
                'c_company': request.POST['c_company'],
                'c_email': request.POST['c_email'],
                'c_phone_number': request.POST['c_phone_number'],
                'c_street_address1': request.POST['c_street_address1'],
                'c_street_address2': request.POST['c_street_address2'],
                'c_town_or_city': request.POST['c_town_or_city'],
                'c_county': request.POST['c_county'],
                'c_postcode': quote.c_postcode,
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'service': request.POST['service'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
            }
        else:
            form_data = {
                'd_contact_name': request.POST['d_contact_name'],
                'd_company': request.POST['d_company'],
                'd_email': request.POST['d_email'],
                'd_phone_number': request.POST['d_phone_number'],
                'd_street_address1': request.POST['d_street_address1'],
                'd_street_address2': request.POST['d_street_address2'],
                'd_town_or_city': request.POST['d_town_or_city'],
                'd_county': request.POST['d_county'],
                'd_postcode': quote.d_postcode,
                'c_contact_name': request.POST['c_contact_name'],
                'c_company': request.POST['c_company'],
                'c_email': request.POST['c_email'],
                'c_phone_number': request.POST['c_phone_number'],
                'c_street_address1': request.POST['c_street_address1'],
                'c_street_address2': request.POST['c_street_address2'],
                'c_town_or_city': request.POST['c_town_or_city'],
                'c_county': request.POST['c_county'],
                'c_postcode': quote.c_postcode,
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'service': request.POST['service'],
                'spec_service': request.POST['spec_service'],
                'height1': request.POST['height1'],
                'length1': request.POST['length1'],
                'width1': request.POST['width1'],
                'weight1': request.POST['weight1'],
                'height2': request.POST['height2'],
                'length2': request.POST['length2'],
                'width2': request.POST['width2'],
                'weight2': request.POST['weight2'],
                'height3': request.POST['height3'],
                'length3': request.POST['length3'],
                'width3': request.POST['width3'],
                'weight3': request.POST['weight3'],
                'height4': request.POST['height4'],
                'length4': request.POST['length4'],
                'width4': request.POST['width4'],
                'weight4': request.POST['weight4'],
                'bookers_email': request.POST['bookers_email'],
                'bookers_phone_number': request.POST['bookers_phone_number'],
            }
        quote = get_object_or_404(Quote, quote_ref=quote_ref)
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = Bookings()
            booking = booking_form.save()
            booking.booking_ref = quote_ref
            booking.price = quote.quote
            booking.items = quote.items
            booking.overall_weight = quote.overall_weight
            booking.overall_volume = quote.overall_volume
            booking.save()

            context = {
                'booking_form': booking_form
            }

            return redirect(reverse(
                'add_to_bag', args=[quote_ref]))

    context = {
        'quote': quote,
        'booking_form': booking_form
    }

    return render(request, 'quote/details.html', context)
