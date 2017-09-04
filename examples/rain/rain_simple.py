from gpiozero import StatusZero
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

sz = StatusZero('dundee', 'cambridge', 'sheffield')

while True:
    if is_raining('Dundee', 'GB'):
        sz.dundee.red.on()
        sz.dundee.green.off()
    else:
        sz.dundee.green.on()
        sz.dundee.red.off()

    if is_raining('Cambridge', 'GB'):
        sz.cambridge.red.on()
        sz.cambridge.green.off()
    else:
        sz.cambridge.green.on()
        sz.cambridge.red.off()

    if is_raining('Sheffield', 'GB'):
        sz.sheffield.red.on()
        sz.sheffield.green.off()
    else:
        sz.sheffield.green.on()
        sz.sheffield.red.off()

    sleep(60*60)  # check every hour
