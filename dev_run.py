"""
Passing this file to manage.py will allow print statments put in the views.py to be seen in terminal.
useful for not having to go back top the browsert during initial development

Usage: python manage.py shell < dev_run.py
"""

from dog_api_app.views import DogImages
from chuck_norris_api_app.views import ChuckNorrisJoke
from rest_framework.test import APIRequestFactory
from django.core.serializers import serialize

dog_request = APIRequestFactory().get('/api/v1/dog_image')
cn_request = APIRequestFactory().get('api/v1/chuck_norris_joke')

DogImages.as_view()(dog_request)
ChuckNorrisJoke.as_view()(cn_request)




