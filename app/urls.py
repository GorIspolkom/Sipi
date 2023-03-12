from django.urls import path
from .views import *

urlpatterns = [
    path('all_devices/', all_devices),
    path('all_policy/', all_policy),
    path('add_device/', add_device)
]
