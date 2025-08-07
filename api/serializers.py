from rest_framework import serializers
from .models import Autores

class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'
        
