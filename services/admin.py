from django.contrib import admin

# Register your models here.
from .models import Service, Service_Type

admin.site.register(Service)
admin.site.register(Service_Type)
