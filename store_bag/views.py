from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from quote.models import Quote, Bookings


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'store_bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a booking to the bag """

    quote = get_object_or_404(Quote, quote_ref=item_id)
    bag = request.session.get('bag', {})

    bag[item_id] = item_id
    messages.success(request,
                     f'Added collection from \
    {quote.c_postcode} to your bag (ref: {item_id})')

    request.session['bag'] = bag

    return redirect(reverse('home'))


def remove_from_bag(request, item_id):
    """ remove the booking from the bag """

    try:
        booking = get_object_or_404(Bookings, booking_ref=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed collection from \
    {booking.c_postcode} from your bag (ref: {item_id})')
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
