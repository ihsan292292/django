from django.db import models

class book(models.Model):
    Accno = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=200)

    def __str__(self):
        return self.Accno
