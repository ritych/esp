from django.contrib import admin

from device.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ip_address",
        "description",
        "firmware_path",
    ]
    list_per_page = 20
