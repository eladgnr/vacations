# vacations/utils.py
import requests


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
