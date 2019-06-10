from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    sun = models.CharField(max_length=100)
    water = models.CharField(max_length=100)
    soil = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name 