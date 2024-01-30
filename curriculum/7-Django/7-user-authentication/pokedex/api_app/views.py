from rest_framework.views import APIView
from rest_framework.response import Response
import requests # <== import requests so we can utilize it within our CBV to make API calls
from requests_oauthlib import OAuth1 #<== import OAuth1 which will essentially authenticate our keys when we send a request
from pokedex_proj.settings import env
import pprint

pp = pprint.PrettyPrinter(indent=2, depth=2)

class Noun_Project(APIView):
    # In our CBV lets create a method to interact with the NounAPI
    def get(self, request, types):
        # let's grab this body from the `get started` documentation from the NounAPI 
        auth = OAuth1(env.get("API_KEY"), env.get("SECRET_KEY")) #<== for now place your corresponding keys here
        endpoint = f"http://api.thenounproject.com/icon/{types}"

        response = requests.get(endpoint, auth=auth) # notice with axios we had to wait for the promise to be completed, with requests it know to pause the program and wait until it receives a response
        # print(response.content) # we can see that the content within this response comes back as a binary string lets fix that
        responseJSON = response.json() # by calling the .json() method we are turning this request into a Python Dictionary that we can manipulate
        # pp.pprint(responseJSON)
        # print(responseJSON['icon']['preview_url'])
        return Response(responseJSON['icon']['preview_url'])