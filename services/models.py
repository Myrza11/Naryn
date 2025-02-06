from django.db import models
from django.core.exceptions import ValidationError
from register.models import CustomUser


class Service_Type(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.IntegerField()
    service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE)

    @classmethod
    def filter_services(service, min_price, max_price, service_type):
        queryset = service.objects.all()

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)

        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        if service_type is not None:
            service_type = Service_Type.objects.get(id=service_type.id)
            queryset = queryset.filter(service_type=service_type)

        return queryset

    def clean(self):
        if self.price <= 0:
            raise ValidationError({"price": "Price must be greater than 0."})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)