
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

class DogImages(APIView):
    def get(self, request):

        print('Hello')

        endpoint = 'https://api.thedogapi.com/v1/images/search?'
        # Dog api can work or without api key
        try:
            auth = OAuth1(os.environ['DOG_KEY'])
            response = requests.get(endpoint, auth=auth) # Get request, with api key
        except KeyError:
            response = requests.get(endpoint) # Get request, without api key

        response = requests.get(endpoint) # Get request, without api key
        #response = requests.get(endpoint, auth=auth) # Get request, with api key

        response_jsoned = response.json()
        print(response_jsoned)

        dog_url_img = response_jsoned[0]['url']
        print(f'dog_url_img = [{dog_url_img}]')
        context = { 'image': dog_url_img }
        return render(request, 'template.html', context)
        #return Response(response_jsoned)
