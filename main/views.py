from datetime import datetime, timedelta

from django.shortcuts import render

from device.models import Device
from main.models import Data
import json
from django.core.serializers import serialize


def device_chart(request):
    devices = Device.objects.all()
    chart_data = None
    device_id = None
    start_date = None
    end_date = None

    if request.method == 'POST':
        device_id = request.POST.get('device_id')
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        # Преобразуем даты из строк в datetime объекты
        try:
            if start_date_str:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            if end_date_str:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                # Добавляем время 23:59:59 для конечной даты
                end_date = end_date.replace(hour=23, minute=59, second=59)
        except (ValueError, TypeError):
            pass

        # Фильтрация данных
        queryset = Data.objects.all()

        if device_id:
            queryset = queryset.filter(device_id=device_id)

        if start_date:
            queryset = queryset.filter(timestamp__gte=start_date)

        if end_date:
            queryset = queryset.filter(timestamp__lte=end_date)

        queryset = queryset.order_by('timestamp')

        # Подготовка данных для графика
        chart_data = {
            'timestamps': [item.timestamp.strftime('%H:%M') for item in queryset],
            'param1': [float(item.param1) if item.param1 != '-' else None for item in queryset],
            'param2': [float(item.param2) if item.param2 != '-' else None for item in queryset],
        }

    return render(request, 'main/device_chart.html', {
        'devices': devices,
        'chart_data': json.dumps(chart_data) if chart_data else None,
        'selected_device': int(device_id) if device_id else None,
        'start_date': start_date.strftime('%Y-%m-%d') if start_date else '',
        'end_date': end_date.strftime('%Y-%m-%d') if end_date else '',
    })
