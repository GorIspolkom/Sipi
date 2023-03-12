from django.db import models
from django.contrib.auth.models import User


def find_profile_by_user(user):
    return Profile.objects.get(user=user)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=30, default=0)

    def __str__(self):
        return self.user.username

    pass
