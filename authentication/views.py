from .serializers import UserSerializer
from .models import Usuarios

import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.hashers import make_password

class UsuarioView(APIView):
    def post(self, request):       
        if request.method == 'POST':
            jd = json.loads(request.body)
            Usuarios.objects.create(username=jd['username'], first_name=jd['first_name'],last_name=jd['last_name'],email=jd['email'],
            password=make_password(jd['password']))
            datos={'msg':'ok'}
            return Response(datos, status=status.HTTP_201_CREATED) 
        else:
            datos={'msg':'no registrado'}
            return Response(datos, status=status.HTTP_400_BAD_REQUEST)  


class CustomUserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuarios.objects.all()