from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories, name='categories'),
    path('all_products', views.all_products, name='products'),
]
