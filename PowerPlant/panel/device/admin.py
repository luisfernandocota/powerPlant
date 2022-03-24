from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from panel.device.models import *
from panel.readings.models import Reading

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    readonly_fields=('has_maintenance',)
    def save_model(self, request, obj, form, change):
        try:
            device = Device.objects.get(pk=obj.pk)
            if change:

                if str(form.cleaned_data['statusDevice']).startswith('En man') and obj.has_maintenance == False:
                    obj.has_maintenance = True

                    Maintenance.objects.create(device=device)
                if str(form.cleaned_data['statusDevice']).startswith('En oper') and obj.has_maintenance == True:
                    obj.has_maintenance = False

                Reading.objects.create(device=device, typeDevice=device.typeDevice,currentPower=form.cleaned_data['currentPower'])
        except ObjectDoesNotExist:
            pass
        super().save_model(request, obj, form, change)

admin.site.register(Device, DeviceAdmin)
admin.site.register(TypeDevice)
admin.site.register(StatusDevice)
