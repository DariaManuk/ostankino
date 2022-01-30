import requests
from distance import lonlat_distance as dis
from math import sqrt


def koord(name):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={name}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['Point'][
            'pos'].split()
        toponym = [float(i) for i in toponym]
        return toponym


print('Введите адрес')
L = dis(koord('Останкинская башня, Москва'), koord(input()))
h_2 = (L / 1000 / 3.6 - sqrt(525)) ** 2
print("Высота приёмной антенны =", h_2, "м")
