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

sz = StatusZero('dundee', 'cambridge', 'sheffield')

statuses = {
    sz.peterborough: is_raining('Dundee', 'GB'),
    sz.cambridge: is_raining('Cambridge', 'GB'),
    sz.sheffield: is_raining('Sheffield', 'GB'),
}

for strip, rain in statuses.items():
    strip.red.source = rain
    strip.red.source_delay = 60*60
    strip.green.source = negated(strip.red.values)

pause()
