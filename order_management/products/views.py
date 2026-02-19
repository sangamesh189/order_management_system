from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import product_serializer,product_serializer_detail
from .models import product

class view_products(APIView):
    serializers_class = product_serializer

    def get(self,request,name = None,*args,**kwargs):
        if name:
            Product = product.objects.get(name = name)
            serializer = product_serializer_detail(Product)
            return Response(serializer.data,status=status.HTTP_200_OK)

        qs = product.objects.all()

        return Response(
            {"data":self.serializers_class(qs,many=True).data},
            status=status.HTTP_200_OK
        )