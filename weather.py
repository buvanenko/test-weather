
import requests

url = "https://api.open-meteo.com/v1/forecast"

def get(lat: float, lon: float) -> dict:
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m",
        "daily": "temperature_2m_max",
    }
    response = requests.get(url, params=params)
    return response.json()
