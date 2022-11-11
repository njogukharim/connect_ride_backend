from django.db import models
from django.utils import timezone
import datetime

def _get_file_extension(filename):
    return filename.split('.')[-1]

def upload_vehicle_images(image, filename):
    return f"vehicles/images/{timezone.now()}.{_get_file_extension(filename)}"


class User(models.Model):
    id = models.UUIDField
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, unique=True)
    phone_no = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15, blank=False, null = False)


class Category(models.Model):
    id = models.UUIDField
    name = models.CharField(max_length=20, null=False, blank=False)


class VehicleImages(models.Model):
    front_img = models.FileField(upload_to=upload_vehicle_images, max_length=255)
    back_img = models.FileField(upload_to=upload_vehicle_images, max_length=255)
    left_side_img = models.FileField(upload_to=upload_vehicle_images, max_length=255)
    right_side_img = models.FileField(upload_to=upload_vehicle_images, max_length=255)
    interior_front_img = models.FileField(upload_to=upload_vehicle_images, max_length=255)
    interior_back_img = models.FileField(upload_to=upload_vehicle_images, max_length=255)
    boot_img = models.FileField(upload_to=upload_vehicle_images, max_length=255)


class Vehicle(models.Model):
    brand_name = models.CharField(max_length =255, null=False, blank=False)
    model = models.CharField(max_length = 20, null=False, blank= False)
    top_speed = models.CharField(max_length=8, null=False, blank=False)
    seats = models.IntegerField(max_length=3, null=False, blank=False)
    transmission = models.CharField(max_length=12, null=False, blank=False)
    rates = models.DecimalField(decimal_places=2, max_digits=5, null=False, blank=False)
    plate_no = models.CharField(max_length=7, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    images = models.ForeignKey(VehicleImages, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['category', 'plate_no']


class Order(models.Model):
    pick_up = models.TimeField
    drop_off = models.TimeField
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
