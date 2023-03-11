from django.db import models
import datetime


def get_all_plates():
    return Plate.objects.all()


def get_all_policy():
    return Policy.objects.all()


class Plate(models.Model):
    ip_address = models.GenericIPAddressField()
    hostname = models.CharField(max_length=45)
    is_active = models.BooleanField(default=False)
    user = models.CharField(max_length=20, default='root')
    password = models.CharField(max_length=45, default='!QAZxsw2')

    def __str__(self):
        return self.hostname

    pass


class Policy(models.Model):
    name = models.CharField(max_length=30)
    playbook_path = models.CharField(max_length=50)
    inventory = models.CharField(max_length=50)
    plates = models.ManyToManyField(Plate)

    def __str__(self):
        return self.name

    pass


class Record(models.Model):
    policy_id = models.OneToOneField(Policy, on_delete=models.CASCADE)
    execution_time = models.DateTimeField(default=datetime.datetime.now())
    log = models.TextField()
    pass


# Create your models here.
