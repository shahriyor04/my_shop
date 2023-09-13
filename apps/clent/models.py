from django.db import models
from django.db.models import Model, CharField, DecimalField, ForeignKey, CASCADE
from prodct.models import Product


class Client(Model):
    username = CharField(max_length=200)
    phone = CharField(max_length=9)
    location = CharField(max_length=50)
    product = ForeignKey(Product, on_delete=CASCADE)
    the_number = DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'client'
