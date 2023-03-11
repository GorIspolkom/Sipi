from django.shortcuts import render
from .models import get_all_plates, get_all_policy


def all_devices(request):
    return render(request, 'devices.html', context={'plates': get_all_plates()})


def all_policy(request):
    return render(request, 'policy.html', context={'policy': get_all_policy()})

# Create your views here.
