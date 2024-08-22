from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    addressr=models.CharField(max_length=100)
    books=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
