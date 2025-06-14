from django.urls import path

from main import views

urlpatterns = [
    path('data/', views.device_chart, name='data'),
]
