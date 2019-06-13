from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Plant, Accessory, Photo
from .forms import WateringForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'plantcollectorlab'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    accessories_plant_doesnt_have = Accessory.objects.exclude(id__in = plant.accessories.all().values_list('id'))
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'accessories': accessories_plant_doesnt_have, 'watering_form': watering_form})

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants/'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['sun', 'water', 'soil', 'color']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

class AccessoryList(ListView):
    model = Accessory

class AccessoryDetail(DetailView):
    model = Accessory

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['name', 'color']

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'

def assoc_access(request, plant_id, accessory_id):
    Plant.objects.get(id=plant_id).accessories.add(accessory_id)
    return redirect('detail', plant_id=plant_id)

def unassoc_access(request, plant_id, accessory_id):
    Plant.objects.get(id=plant_id).accessories.remove(accessory_id)
    return redirect('detail', plant_id=plant_id)

def add_photo(request, plant_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, plant_id=plant_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', plant_id=plant_id)