from rest_framework import viewsets
from .models import Fabric
from .serializers import FabricSerializer

class FabricViewSet(viewsets.ModelViewSet):
    queryset = Fabric.objects.all()
    serializer_class = FabricSerializer
