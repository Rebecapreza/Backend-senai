from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Autores
from .serializers import AutorSerializers

class AutoresView(ListCreateAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutorSerializers

