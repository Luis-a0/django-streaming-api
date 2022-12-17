from rest_framework import serializers
from .models import Audiovisual, Tipo, Genero

class AudiovisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiovisual
        fields = ('id', 'nombre', 'generos', 'tipo', 'visualizaciones', 'puntaje')
        read_only_fields = ('id', )