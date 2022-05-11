from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from durin.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductsList(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        pass

    def post(self, rerquest, format=None):
        pass


class ProductDetail(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get(self, request, pk, format=None):
        pass

    def patch(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass