# Response is utilized to hand API behaviour
from rest_framework.views import APIView, Response
# Authenticates a user with public and secret keys
from requests_oauthlib import OAuth1
# Allows us to interact with .env files
from dotenv import load_dotenv
# Needed to load a template
from django.shortcuts import render
# Pythons user friendly way to make requests to API's
import requests
# Used to read .env file
import os

load_dotenv()

class ChuckNorrisJoke(APIView):
    
    def get(self, request):
        endpoint = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(endpoint) # Get request, without api key
        response_jsoned = response.json()
        print(response_jsoned)

        joke_str = response_jsoned['value']
        print(f'joke_str = [{joke_str}]')
        context = { 'joke': joke_str }
        return render(request, 'cn_template.html', context)
        #return Response(response_jsoned)