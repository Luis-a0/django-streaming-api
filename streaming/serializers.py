from rest_framework import serializers
from .models import Audiovisual, Tipo, Genero, AudiovisualUser

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'nombre')
        read_only_fields = ('id', )

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('nombre', 'Audiovisual',)
        read_only_fields = ('id', )

    class AnidadoAudiovisualSerializer(serializers.ModelSerializer):

        class Meta:
            model = Audiovisual
            fields = ('id', 'nombre', 'tipo', 'visualizaciones', 'puntaje')

    Audiovisual = AnidadoAudiovisualSerializer(
        many=True, read_only=True)

    Audiovisual = AnidadoAudiovisualSerializer(many=True, source='media_genero')

class AudiovisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiovisual
        fields = '__all__'
    
    class AnidadoGeneroSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genero
            fields = '__all__'

    generos = AnidadoGeneroSerializer(many=True)

class AudiovisualUserSerializer(serializers.ModelSerializer):

    media = AudiovisualSerializer(read_only=True)

    class Meta:
        model = AudiovisualUser
        fields = ['media', 'visto', 'puntuacion']