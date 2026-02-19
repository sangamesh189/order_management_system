from rest_framework import serializers
from .models import product

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['name','price',]

class product_serializer_detail(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"

