from django.db.models import ExpressionWrapper, F
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from prodct.models import Product
from .models import Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        count = validated_data.get('count')
        product_id = validated_data.get('product')

        if not isinstance(count, int) or count <= 0:
            raise ValidationError("Invalid 'count' value. It should be a positive integer.")

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product with the specified ID does not exist.")

        if count <= product.the_number:
            product.the_number = ExpressionWrapper(F('the_number') - count, output_field=IntegerField())
            product.save()
        else:
            raise ValidationError("Not enough stock to complete this purchase.")

        return super().create(validated_data)

