from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_fuel_form, name='test'),
]
