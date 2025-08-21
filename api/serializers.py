from rest_framework import serializers
from .models import Autores, Editora, Livro


class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'

class EditoraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class LivroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        
