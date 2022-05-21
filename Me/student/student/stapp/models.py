from django.db import models

# Create your models here.

class std(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    m1 = models.CharField(max_length=100)
    m2 = models.CharField(max_length=100)
    m3 = models.CharField(max_length=100)
    total_mark = models.CharField(max_length=100)
    avg_mark = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
