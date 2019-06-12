from django.db import models
from django.urls import reverse

# Create your models here.
WATERED = (
    ('W', 'With Plant Food'),
    ('O', 'Without Plant Food')
)

class Plant(models.Model):
    name = models.CharField(max_length=100)
    sun = models.CharField(max_length=100)
    water = models.CharField(max_length=100)
    soil = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

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