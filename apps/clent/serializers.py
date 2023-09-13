from django.db.models import ExpressionWrapper, F
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer

from prodct.models import Product
from .models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        the_number = validated_data.get('the_number')
        product = validated_data['product']
        if the_number < 0:
            raise ValidationError("to'gri son kirit dalbo'yop")
        if not isinstance(product, Product):
            product = get_object_or_404(Product, pk=product)
        if the_number <= product.the_number:
            product.the_number -= the_number
            product.save()
            return super().create(validated_data)
        raise ValidationError("Buncha mahsulot yo'q")

