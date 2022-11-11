from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from main.serializers import *
from main.models import Order, Category, Vehicle, VehicleImages


class CategoryListApiView(generics.ListCreateAPIView):
    serializer_class = Categoryserializer
    queryset = Category.objects.all()

class CategoryDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Categoryserializer
    queryset = Category.objects.all()

class OrderListApiView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class VehicleListApiView(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    queryset = [MultiPartParser, FormParser]

class VehicleDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleImagesListApiView(generics.ListCreateAPIView):
    serializer_class = VehicleImageSerializer
    queryset = VehicleImages.objects.all()
    parser_classes = [MultiPartParser, FormParser]

class VehicleImagesDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleImageSerializer
    queryset = VehicleImages.objects.all()