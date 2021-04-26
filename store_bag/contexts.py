from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from quote.models import Quote, Bookings


def bag_contents(request):

    bag_items = []
    total = 0
    bag = request.session.get('bag', {})
    product_count = 0

    for item_id, item_data in bag.items():

        booking = Bookings.objects.get(booking_ref=item_id)
        total += booking.price
        subtotal = booking.price
        bag_items.append({
            'booking_ref': item_id,
            'weight': booking.overall_weight,
            'volume_weight': booking.overall_volume,
            'booking': booking,
            'subtotal': subtotal,
        })

    product_count += len(bag_items)

    if product_count >= settings.TEN_PERCENT_THRESHOLD:
        ten_percent = total / 10
        ten_percent_delta = 0
    else:
        ten_percent = 0
        ten_percent_delta = settings.TEN_PERCENT_THRESHOLD - product_count

    grand_total = total - ten_percent

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'ten_percent_delta': ten_percent_delta,
        'ten_percent_threshold': settings.TEN_PERCENT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
