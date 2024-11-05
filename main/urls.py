from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FabricViewSet, UserProfileViewSet, OrderViewSet, register_user

router = DefaultRouter()
router.register(r'fabrics', FabricViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),  # Registration endpoint
]
