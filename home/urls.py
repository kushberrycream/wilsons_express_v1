from django.urls import path
from . import views
from quote.views import quote


urlpatterns = [
    path('', views.index, name='home'),
    path('covid/', views.covid, name='covid'),
    path('quote/', quote, name='quote'),
]
