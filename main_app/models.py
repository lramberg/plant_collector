from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
WATERED = (
    ('W', 'With Plant Food'),
    ('O', 'Without Plant Food')
)

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})

class Plant(models.Model):
    name = models.CharField(max_length=100)
    sun = models.CharField(max_length=100)
    water = models.CharField(max_length=100)
    soil = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Watering(models.Model):
    date = models.DateField()
    watered = models.CharField(
        max_length=1,
        choices=WATERED,
        default=WATERED[0][0]
        )
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_watered_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for plant_id: {self.plant_id} @ {self.url}"