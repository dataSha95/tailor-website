from django.db import models
from django.contrib.auth.models import User

class Fabric(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price_per_meter = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.color}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE)  # Assuming Fabric model is already set up
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

