from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.conf import settings

from django.forms.models import model_to_dict
from panel.device.models import Device
from panel.readings.models import Reading
from panel.core.utils import filters_by_request
# Create your views here.
class DeviceListViews(View):
    def get(self, request):
        filters = filters_by_request(request)
        try:
            if filters:
                data = Device.objects.filter(**filters)
            else:
                data = Device.objects.all()
        except Device.DoesNotExist:
            data = {}
        return JsonResponse(list(data.values()), safe=False)


class DeviceDetailViews(View):
    def get(self, request, pk):
        try:
            device = Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            device = {}
        return JsonResponse(model_to_dict(device))


class ReadingsViews(View):
    def get(self, request):
        try:
            total = request.GET.get('total')
            if total:
                readings = Reading.get_total_power(request.GET['total'])
                return JsonResponse(readings, safe=False)

            else:
                readings = Reading.objects.all()
                return JsonResponse(list(readings.values()), safe=False)
        except Reading.DoesNotExist:
            readings = {}
            return JsonResponse(list(readings.values()), safe=False)

class ReadingsDeviceViews(View):
    def get(self, request, pk):
        try:
            readings = Reading.objects.filter(device__pk=pk)
        except Reading.DoesNotExist:
            readings = {}
        return JsonResponse(list(readings.values()), safe=False)

class ReadingsTypeDeviceViews(View):
    def get(self, request, pk):
        try:
            readings = Reading.objects.filter(typeDevice=pk)
        except Reading.DoesNotExist:
            readings = {}
        return JsonResponse(list(readings.values()),safe=False)

        