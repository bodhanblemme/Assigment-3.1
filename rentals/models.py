from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    daily_price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Rental(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.equipment} - {self.client}"