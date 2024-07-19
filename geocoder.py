
import requests
import config

url = 'https://geocode-maps.yandex.ru/1.x/'

def get(address: str):
    """
    Функция принимает на вход адрес и возвращает словарь с координатами этого адреса.

    :param address: адрес, для которого нужно получить координаты
    :return: словарь с координата адреса в формате {'lat': 'широта', 'lon': 'долгота'}
    """
    params = {
        'apikey': config.GEOCODER_API_KEY,
        'geocode': address,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] == 0:
        return None, None
    
    coords = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
    return coords[1], coords[0]
