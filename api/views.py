from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autores, Editora, Livro
from .serializers import AutorSerializers, EditoraSerializers, LivroSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class AutoresView(ListCreateAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutorSerializers

class AutoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutorSerializers

class EditoraView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializers

class EditoraDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = AutorSerializers

class LivroView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers

class LivroDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers


@api_view(['GET', "POST"])
def visualizacao_autor(request):
    if request.method == 'GET':
        queryset = Autores.objects.all()
        serializer = AutorSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializers (data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        

