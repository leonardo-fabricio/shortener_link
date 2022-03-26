from django.db import models

# Create your models here.

class Link(models.Model):
    hash = models.CharField(max_length=150, unique= True)
    url = models.CharField(max_length=1000)
    short_link = models.CharField(max_length=200, blank = True) 