from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def all_products(request):
    """ A view to return all products, including sorting
    and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def all_categories(request):
    """ A view to return all categories, including sorting
    and search queries """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/categories.html', context)
