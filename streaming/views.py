from django.shortcuts import render

from rest_framework import (viewsets, permissions,status,
                            filters, views, authentication)
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AudiovisualSerializer, AudiovisualUser
from .models import Audiovisual, AudiovisualUser

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


class MediaUserViewSet(views.APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        queryset = AudiovisualUser.objects.filter(user=self.request.user)
        serializer = AudiovisualSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            media = Audiovisual.objects.get(id=request.data['id'])
        except Audiovisual.DoesNotExist:
            return Response(
                {'status': 'Film not found'},
                status=status.HTTP_404_NOT_FOUND)

        media_user, created = AudiovisualUser.objects.get_or_create(
            user=request.user, media=media)

        media_user.puntuacion = request.data.get('puntuacion', 0)
        media_user.visto = request.data.get('visto', False)

        if int(media_user.state) == 0:
            media_user.delete()
            return Response(
                {'status': 'Deleted'}, status=status.HTTP_200_OK)

        else:
            media_user.save()

        return Response(
            {'status': 'Saved'}, status=status.HTTP_200_OK)