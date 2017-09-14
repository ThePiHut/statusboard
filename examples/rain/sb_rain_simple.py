from gpiozero import StatusBoard
from gpiozero.tools import negated
import json
import requests
from time import sleep

KEY = 'ENTER API KEY HERE'  # http://openweathermap.org/
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast?APPID={}'.format(KEY)

with open('cities.json') as f:
    cities = json.load(f)

def is_raining(city, country):
    city_id = cities[country][city]
    url = '{}&id={}'.format(BASE_URL, city_id)
    j = requests.get(url).json()
    return 'rain' in j['list'][2]

sb = StatusBoard('cambridge', 'sheffield', 'nottingham')

while True:
    if is_raining('Cambridge', 'GB'):
        sb.cambridge.lights.red.on()
        sb.cambridge.lights.green.off()
    else:
        sb.cambridge.lights.green.on()
        sb.cambridge.lights.red.off()

    if is_raining('Sheffield', 'GB'):
        sb.sheffield.lights.red.on()
        sb.sheffield.lights.green.off()
    else:
        sb.sheffield.lights.green.on()
        sb.sheffield.lights.red.off()

    if is_raining('Nottingham', 'GB'):
        sb.nottingham.lights.red.on()
        sb.nottingham.lights.green.off()
    else:
        sb.nottingham.lights.green.on()
        sb.nottingham.lights.red.off()

    sleep(60*60)  # check every hour
