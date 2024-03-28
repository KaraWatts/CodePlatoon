from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from requests_oauthlib import OAuth1
from APItests.settings import env
import pprint
from urllib.parse import quote

pp = pprint.PrettyPrinter(indent=2, depth=2)

# Create your views here.
class Moderator(APIView):
    
    def get(self, request, image):
        print(image, "\n")
        # encoded_image = quote(image)
        params = {"url": image,
                  "key": env.get("KEY")}
        
        # auth = OAuth1(env.get("KEY"))
        endpoint = f"https://api.moderatecontent.com/moderate/?face=true"

        response = requests.get(endpoint, params=params)

        responseJSON = response.json()

        pp.pprint(responseJSON)
        return Response(responseJSON)
        