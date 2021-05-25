"""wilsons_express URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include("allauth.urls")),
    path('', include('home.urls')),
    path('bag/', include('store_bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('contact/', include('contact_form.urls')),
    path('profile/', include('profiles.urls')),
    path('faqs/', include('faqs.urls')),
    path('credit-account/', include('create_account.urls')),
    path('delivery/', include('quote.urls')),
    path('wilsons_admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
