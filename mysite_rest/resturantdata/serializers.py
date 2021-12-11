from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers


from resturantdata import models

class ProductSerializers(serializers.ModelSerializer):

   
    class Meta:
        model=models.Products
        fields='__all__'

