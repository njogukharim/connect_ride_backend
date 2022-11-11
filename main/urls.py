from django.urls import path

from main import views

urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view()),
    path('categories/<uuid:pk>/', views.CategoryDetailApiview.as_view()),
    path('orders/', views.OrderListApiView.as_view()),
    path('orders/<uuid:pk>/', views.OrderDetailApiView.as_view()),
    path('vehicle/', views.VehicleListApiView.as_view()),
    path('vehicle/<uuid:pk>/', views.VehicleDetailApiView.as_view()),
    path('vehicle-images/', views.VehicleImagesListApiView.as_view()),
    path('vehicle-images/<int:pk>', views.VehicleImagesDetailApiView.as_view()),

]