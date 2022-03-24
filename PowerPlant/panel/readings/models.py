from django.db import models
from django_extensions.db.models import TimeStampedModel
from panel.device.models import *
# Create your models here.
class Reading(TimeStampedModel):
    device = models.ForeignKey(Device, related_name='reading_device', on_delete=models.CASCADE)
    typeDevice = models.ForeignKey(TypeDevice, related_name='reading_typeDevice', on_delete=models.CASCADE)
    currentPower = models.SmallIntegerField(verbose_name='Current power')

    class Meta:
            db_table = 'readings'
            verbose_name_plural = 'Readings'

    def __str__(self):
        return '%s' % (self.device.nameDevice)

    @staticmethod
    def get_total_power(pk):
        from django.forms.models import model_to_dict
        data = {'energiaTotal':{}}
        total = Reading.objects.filter(device__pk=pk, device__statusDevice__description__icontains='En oper')\
                        .aggregate(total=models.Sum('currentPower'))
        device = Device.objects.get(pk=pk, statusDevice__description__icontains='En oper')
        data['energiaTotal'].update(total)
        data['energiaTotal'].update(model_to_dict(device))
        return data