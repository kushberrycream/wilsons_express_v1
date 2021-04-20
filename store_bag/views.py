from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product
from quote.models import Quote


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'store_bag/bag.html')


def add_to_bag(request, quote_ref):
    """ Add a quantity of the specified product to the shoppingbag """

    quote = get_object_or_404(Quote, quote_ref=quote_ref)
    bag = request.session.get('bag', {})

    messages.success(request, f'Added {quote_ref} to your bag')

    request.session['bag'] = bag

    return redirect(reverse('details', args=[quote.quote_ref]))


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the
    specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name}\
                        quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
