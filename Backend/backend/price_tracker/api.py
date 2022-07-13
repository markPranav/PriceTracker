from functools import partial
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from durin.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from price_tracker.serializer import ProductSerializer
from .models import Product

class ProductsList(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        

    def post(self, request, format=None):
        
        serializer=ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
        
        
        
        


class ProductDetail(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_objects(self,pk):
        try:
            product=Product.objects.get(id=pk)
            return product
        except Product.DoesNotExist:
            raise Http404
        
        
    def get(self, request, pk, format=None):
        product=self.get_objects(pk=pk)
        serializer=ProductSerializer(product)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        

    def patch(self, request, pk, format=None):
        product=self.get_objects(pk=pk)
        serializer=ProductSerializer(product,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        product=self.get_objects(pk=pk)
        
        product.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)