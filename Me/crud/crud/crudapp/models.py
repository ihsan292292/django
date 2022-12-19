from django.db import models

class stud(models.Model):
    sid = models.CharField(max_length=100,primary_key=True)
    sname = models.CharField(max_length=100)
    sadds = models.CharField(max_length=100)
    scity = models.CharField(max_length=100)
    semail = models.CharField(max_length=100)
    sphon = models.IntegerField()
    
