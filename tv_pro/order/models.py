from django.db import models

# Create your models here.
class Order(models.Model):
    type_order = models.CharField(verbose_name="Тип заказа",max_length=30, blank=True, null=True)
    name = models.CharField(verbose_name="Имя заказчика",max_length= 50, blank=True, null=True)
    time_call = models.CharField(verbose_name="Звонить в", max_length=50, blank=True, null=True)
    phone_number = models.CharField(verbose_name="Телефон", max_length=12, blank=True, null=True)

    def __str__(self):
        return "%s %s  %s  %s " % (self.type_order, self.name, self.time_call, self.phone_number)

