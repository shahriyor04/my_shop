from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from .serializers import ClientSerializer
from .models import Client


class ClientApiModelViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    http_method_names = ['get', 'post']
    parser_classes = [MultiPartParser]







