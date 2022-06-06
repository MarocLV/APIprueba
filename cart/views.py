from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def mensaje_carrito(request):
    mensaje = {'msg' : 'estás en la API de carrito'}
    return Response(mensaje, status=status.HTTP_200_OK)