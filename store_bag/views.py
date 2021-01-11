from django.shortcuts import render


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'store_bag/bag.html')
