from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Stationary','Stationary'),
    ('Electrocis','Electronics'),
    ('Food','Food'),
)
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices= CATEGORY,null=True)
    

    def __str__(self):
     return f'{self.name}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE,null=True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} orderd by {self.staff.username}' 