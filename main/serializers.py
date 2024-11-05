from rest_framework import serializers
from .models import Fabric

class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabric
        fields = ['id', 'name', 'color', 'price_per_meter']
