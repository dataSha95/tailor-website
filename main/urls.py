from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FabricViewSet, register_user

router = DefaultRouter()
router.register(r'fabrics', FabricViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),  # Registration endpoint
]




