from django.db import models

# Create your models here.
class rate(models.Model):
    name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    taste=models.CharField(max_length=100)
    color=models.CharField( max_length=100)
    price=models.IntegerField()
