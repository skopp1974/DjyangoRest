from rest_framework import serializers
from .models import Rig

class ValidateFormSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=32)
    

class RigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rig
        fields = '__all__'
