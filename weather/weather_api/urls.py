from django.urls import path
from weather_api import views
urlpatterns = [
    path('',views.WeatherAPIViews.as_view())
]
