from django.db import models


class Employee (models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Store (models.Model):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Visit (models.Model):
    date = models.DateTimeField('Дата', auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, blank=True, null= True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    #def __str__(self):
     #   return self.store
