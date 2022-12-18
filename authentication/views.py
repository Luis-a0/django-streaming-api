from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        user = request.data.get('user', None)
        password = request.data.get('password', None)
        user = authenticate(username=user, password=password)
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
