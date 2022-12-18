from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AudiovisualSerializer
from .models import Audiovisual, Tipo, Genero

class AudiovisualViewSet(viewsets.ModelViewSet):
    queryset = Audiovisual.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AudiovisualSerializer

    # filtros
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter]

    filterset_fields = ['nombre', 'tipo__nombre', 'generos__nombre', 'puntaje', 'generos', 'tipo']

    search_fields = ['nombre', 'tipo__nombre', 'generos__nombre']
    ordering_fields = ['nombre', 'tipo__nombre', 'generos__nombre', 'puntaje', 'generos', 'tipo']
