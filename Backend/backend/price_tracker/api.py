from functools import partial
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from durin.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from price_tracker.serializer import ProductSerializer
from .models import PriceHistory, Product
from rest_framework.decorators import api_view
from .scrapers import genericScrapper

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
    

@api_view(['GET'])
def check_products(request):
    """
    List all code snippets, or create a new snippet.
    """
    
    products = Product.objects.all()
    
    for p in products:
        try:
            prices=genericScrapper(p.url)
        except Exception as e:
            print(e)
            #Website is down, need to update availability
            
            
        history=PriceHistory.objects.filter(product=p).latest('timestamp')
        
        if history.exist()==False:
            temp=PriceHistory(product=p,availability=prices[2],actual_price=prices[1],sell_price=prices[0])
            temp.save()
            continue
            
                      
        if prices[0]!=history.sell_price and prices[2]!=history.availability:
            temp=PriceHistory(product=p,availability=prices[2],actual_price=prices[1],sell_price=prices[0])
            temp.save()
            
                 
    
    
    return Response(status=status.HTTP_200_OK)