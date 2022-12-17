from rest_framework import viewsets, permissions
from .serializers import AudiovisualSerializer
from .models import Audiovisual, Tipo, Genero

class AudiovisualViewSet(viewsets.ModelViewSet):
    queryset = Audiovisual.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AudiovisualSerializer