from gpiozero import StatusBoard
from gpiozero.tools import negated
import requests
from signal import pause

def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    while True:
        r = requests.get(url)
        yield text in r.text

sb = StatusBoard()

people = ['Donald Trump', 'Kim Jong-Un', 'Theresa May']

for strip, person in zip(sb, people):
    strip.lights.red.source = in_the_news(person)
    strip.lights.red.source_delay = 60  # check every hour
    strip.lights.green.source = negated(strip.lights.red.values)

pause()
