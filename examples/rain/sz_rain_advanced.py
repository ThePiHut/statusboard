from gpiozero import StatusZero
from gpiozero.tools import negated
import json
import requests
from signal import pause

KEY = 'ENTER API KEY HERE'  # http://openweathermap.org/
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast?APPID={}'.format(KEY)

with open('cities.json') as f:
    cities = json.load(f)

def is_raining(city, country):
    city_id = cities[country][city]
    url = '{}&id={}'.format(BASE_URL, city_id)
    while True:
        j = requests.get(url).json()
        yield 'rain' in j['list'][2]

sz = StatusZero()

my_cities = ['cambridge', 'sheffield', 'nottingham']

for strip, city in zip(sz, my_cities):
    strip.red.source = is_raining(city, 'GB')
    strip.red.source_delay = 60*60  # check every hour
    strip.green.source = negated(strip.red.values)

pause()
