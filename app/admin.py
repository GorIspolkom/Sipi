from django.contrib import admin
from .models import Plate, Policy, Record

admin.site.register(Plate)
admin.site.register(Policy)
admin.site.register(Record)


class PolicyAdmin(admin.ModelAdmin):
    filter_horizontal = ['plates']
    pass

# Register your models here.
