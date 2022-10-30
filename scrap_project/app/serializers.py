from rest_framework import serializers

from .models import CellData

class CellDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=CellData
        fields='__all__'