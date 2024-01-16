from django.db import models

# Create your models here.
class bank(models.Model):
    name=models.CharField(max_length=250)
    password=models.TextField()
