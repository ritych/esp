from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.v1.endpoints.device import DeviceViewSet


router = DefaultRouter()
router.register(r"devices", DeviceViewSet, basename="devices")

urlpatterns = [
    path("", include(router.urls)),
]
