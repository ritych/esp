from django.db import models

from device.models import Device


class Data(models.Model):
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )
    param1 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Параметр 1'
    )
    param2 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Параметр 2'
    )
    param3 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Параметр 3'
    )
    param4 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name='Параметр 4'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
