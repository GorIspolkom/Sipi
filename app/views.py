from django.shortcuts import render, redirect
from .models import get_all_plates, get_all_policy
from .form import PlateForm


def all_devices(request):
    return render(request, 'app/devices.html', context={'plates': get_all_plates()})


def all_policy(request):
    return render(request, 'app/policy.html', context={'policy': get_all_policy()})


def add_device(request):
    if request.method == 'POST':
        form = PlateForm(request.POST)
        if form.is_valid():
            form.save()
            pass
        return redirect('/devices/all_devices')
    else:
        form = PlateForm()
        return render(request, 'app/add_device.html', context={'form': form})
    pass

# Create your views here.
