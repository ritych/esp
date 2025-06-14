from datetime import datetime, timedelta

from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilterBuilder

from main.models import Data


@admin.register(Data)
class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        "device",
        "param1",
        "param2",
        "param3",
        "param4",
        "timestamp",
    ]
    list_per_page = 50
    list_filter = [
        "device",
        (
            "timestamp",
            DateTimeRangeFilterBuilder(
                title="Дата создания",
                default_start=datetime.now() - timedelta(days=1),
                default_end=datetime.now(),
            ),
        ),
    ]

