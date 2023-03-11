from django.forms import ModelForm, CharField, TextInput
from .models import Profile, User


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['telegram_id']
        pass
    pass


class UserForm(ModelForm):
    username = CharField(max_length=100, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        pass
    pass

