from gpiozero import StatusZero
from gpiozero.tools import negated
import requests
from signal import pause

def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    while True:
        r = requests.get(url)
        yield text in r.text

sz = StatusZero()

people = ['Donald Trump', 'Kim Jong-Un', 'Theresa May']

for strip, person in zip(sz, people):
    strip.red.source = in_the_news(person)
    strip.red.source_delay = 60  # check every hour
    strip.green.source = negated(strip.red.values)

pause()
