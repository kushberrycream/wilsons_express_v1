from django.urls import path
from . import views


urlpatterns = [
    path('quote/', views.quote, name='quote'),
    path('quote/<quote_ref>/', views.partial_quote, name='partial_quote'),
    path('enter-details/<quote_ref>/', views.delivery_details, name='details'),
]
