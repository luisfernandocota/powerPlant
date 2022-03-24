from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from panel.device.models import *
from panel.readings.models import Reading

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            device = Device.objects.get(pk=obj.pk)
            if change:
                Reading.objects.create(device=device, typeDevice=device.typeDevice,currentPower=form.cleaned_data['currentPower'])
        except ObjectDoesNotExist:
            pass
        super().save_model(request, obj, form, change)

admin.site.register(Device, DeviceAdmin)
admin.site.register(TypeDevice)
admin.site.register(StatusDevice)
