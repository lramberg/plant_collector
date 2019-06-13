from django.contrib import admin
from .models import Plant, Watering, Accessory, Photo

# Register your models here.
admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Accessory)
admin.site.register(Photo)