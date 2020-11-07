from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from weather_api.cmpo import is_dateprime
import requests
import json

# Create your views here.

class WeatherAPIViews(APIView):
    def get(self, request, formate=None):
        data = []
        if is_dateprime()==True:
            url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=07043f581b4457354af6878b172972f8'
            data = requests.get(url)
            data = data.json()
             

        return Response({'message':'todays wether','data':data})

        

