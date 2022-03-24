from typing import Type
from django.db import models
from django_extensions.db.models import TimeStampedModel

class TypeDevice(models.Model):
    nameType = models.CharField(verbose_name='Name device', max_length=50)

    class Meta:
        db_table = 'type_devices'
        verbose_name = 'Type device'

    def __str__(self):
        return '%s' % (self.nameType)

class StatusDevice(models.Model):
    description = models.CharField(verbose_name='Description', max_length=100)

    class Meta:
        db_table = 'status_devices'
        verbose_name_plural = 'Status devices'

    def __str__(self):
        return '%s' % (self.description)

# Create your models here.
class Device(TimeStampedModel):
    nameDevice = models.CharField(verbose_name='Name device', max_length=50)
    currentPower = models.SmallIntegerField(verbose_name='Current power')
    typeDevice = models.ForeignKey(TypeDevice, related_name='device_typeDevice', on_delete=models.CASCADE)
    statusDevice = models.ForeignKey(StatusDevice, related_name='device_statusDevice', on_delete=models.CASCADE)

    class Meta:
        db_table = 'devices'
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return '%s - %s (KWh)' % (self.nameDevice, self.currentPower)
