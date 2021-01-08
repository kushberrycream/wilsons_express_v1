from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories, name='store_home'),
    path('packing/', views.all_products, name='categories'),
    path('all_products/', views.all_products, name='products'),
    path('<product_id>/', views.product_detail, name='product_detail'),
]
