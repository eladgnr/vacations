import requests

""" This module contains utility functions for the Vacations app.
It includes functions to fetch weather data for a given country."""


def get_country_weather(country_name):
    try:
        url = f"https://wttr.in/{country_name}?format=j1"
        response = requests.get(url)
        data = response.json()
        current = data['current_condition'][0]
        return {
            'temp_c': current['temp_C'],
            'condition': current['weatherDesc'][0]['value']
        }
    except Exception as e:
        print(f"Weather fetch error for {country_name}: {e}")
        return None
