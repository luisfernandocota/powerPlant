
from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.DeviceListViews.as_view(), name='device_list'),
    path('device/<int:pk>/', views.DeviceDetailViews.as_view(), name="device_detail"),

    path('readings/', views.ReadingsViews.as_view(), name="readings"),
    path('readings/device/<int:pk>/', views.ReadingsDeviceViews.as_view(), name="readings_device"),
    path('readings/device/type/<int:pk>/', views.ReadingsTypeDeviceViews.as_view(), name="readings_type_device"),

    path('maintenances/<int:pk>', views.MaintenanceViews.as_view(), name="maintenances")
]