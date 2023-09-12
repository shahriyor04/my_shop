from django.db import models
from django.db.models import Model, CharField, DecimalField, ImageField, IntegerField, FloatField, ForeignKey, CASCADE


# Create your models here.
class Category(Model):
    name = CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_category'
        ordering = ['-created_at']


class Product(Model):
    name = CharField(max_length=100)
    the_number = IntegerField()
    price = DecimalField(max_digits=10,decimal_places=2)
    stock = FloatField( null = True)
    description = CharField(max_length=1000)
    image = ImageField(upload_to='images/product')
    category = ForeignKey(Category, on_delete=CASCADE)
    brand = CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'prodct_product'
        ordering = ['-created_at']