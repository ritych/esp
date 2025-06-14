from django.db import models


class Device(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название датчика',
    )
    ip_address = models.CharField(
        max_length=255,
        verbose_name="IP address"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    auth_login = models.CharField(
        max_length=255,
        verbose_name="Логин",
    )
    auth_password = models.CharField(
        max_length=255,
        verbose_name="Пароль",
    )
    firmware_path = models.CharField(
        max_length=255,
        verbose_name="Путь для прошивки",
    )
    # TODO Добавить ID устройства

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
