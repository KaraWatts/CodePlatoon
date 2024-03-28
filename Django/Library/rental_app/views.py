from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    )
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import RentalSerializer
from .models import Rental
# Create your views here.

class Rentals(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        rentals = RentalSerializer(many=True)
        return Response(rentals.data)
    

    def post(self, request):
        new_rental = RentalSerializer(data=request.data)
        if new_rental.is_valid():
            new_rental.save()
            return Response(new_rental.data, status=HTTP_201_CREATED)
        return Response(new_rental.errors, status=HTTP_400_BAD_REQUEST)