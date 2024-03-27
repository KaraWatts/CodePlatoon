from django.shortcuts import render
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
    )
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ClientSerializer

# Create your views here.
class Sign_up(APIView):
    def post(self, request):
        request.data['username'] = request.data['email']
        client = Client.objects.create_user(**request.data)
        token = Token.objects.create(user = client)
        return Response({'client': client.email, 'token': token.key}, status=HTTP_201_CREATED)
    
class Log_in(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        client = authenticate(username=email, password=password)
        if client:
            token, created = Token.objects.get_or_create(user=client)
            return Response({"token": token.key, "client": client.email})
        else:
            return Response("No client matching the credentials", status=HTTP_404_NOT_FOUND)

class Log_out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    rentals = serializers.SerializerMethodField()


    def get(self, request):
        client = ClientSerializer(request.user)
        return Response(client.data)

