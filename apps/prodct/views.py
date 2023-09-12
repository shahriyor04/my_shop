from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .permission import ProductPermission, CategoryPermissions
from rest_framework.viewsets import ModelViewSet


class CategoryAPIViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (CategoryPermissions, )
    parser_classes = [MultiPartParser]
    # http_method_names = ( 'GET', 'POST')


class ProductAPIViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (ProductPermission, )
    # permission_classes = (IsAdminUser, )
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ProductSerializer
        else:
            pass

