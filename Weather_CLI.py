# Basic Weather App: Build a simple command-line weather application that fetches and displays current weather data for a user-specified location using an API.

from geopy.geocoders import Nominatim
import requests
import json

def get_lat_lon(city):
    geolocater = Nominatim(user_agent="city-locator")
    try:
        location = geolocater.geocode(city)

        if location:
            lat = location.latitude
            lon = location.longitude
            return lat, lon
        else:
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def get_weather(lat, lon, city):

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

    if response.status_code == 200:
        data = response.json()
        main_data = data["current_weather"]
        temp = main_data["temperature"]

        print(f"Weather in {city}: ")
        print(f"Current Temperature: {temp}°C")
    else:
        print("Error fetching weather data. Please check the city name.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    lat, lon = get_lat_lon(city)
    get_weather(lat, lon, city)