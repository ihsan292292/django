from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=50,unique=True)
    mark1 = models.DecimalField(max_digits=6,decimal_places=2)
    mark2= models.DecimalField(max_digits=6,decimal_places=2)
    mark3 = models.DecimalField(max_digits=6,decimal_places=2)
    total_mark = models.DecimalField(max_digits=6,decimal_places=2)
    avg_mark = models.DecimalField(max_digits=6,decimal_places=2)
    