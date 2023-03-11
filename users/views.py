from django.shortcuts import render
from .models import find_profile_by_user
from .form import ProfileForm, UserForm


def profile(request):
    if request.method == 'POST':
        user_prof = UserForm(request.POST, instance=request.user)
        prof_form = ProfileForm(request.POST, instance=find_profile_by_user(request.user))
        if user_prof.is_valid() and prof_form.is_valid():
            user_prof.save()
            prof_form.save()
            pass
        return render(request, 'registration/profile.html', context={'profile': find_profile_by_user(request.user)})
    else:
        user_prof = UserForm(instance=request.user)
        prof_form = ProfileForm(instance=find_profile_by_user(request.user))
        return render(request, 'registration/profile.html', context={'user_form': user_prof, 'prof_form': prof_form})
    pass


'''
def profile(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'registration/profile.html', context={'profile': find_profile_by_user(request.user)})
'''

# Create your views here.
