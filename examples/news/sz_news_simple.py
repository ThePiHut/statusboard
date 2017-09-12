from gpiozero import StatusZero
import requests
from time import sleep

def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    r = requests.get(url)
    return text in r.text

sz = StatusZero('trump', 'kim', 'may')

while True:
    if in_the_news('Donald Trump'):
        sz.trump.red.on()
        sz.trump.green.off()
    else:
        sz.trump.green.on()
        sz.trump.red.off()

    if in_the_news('Kim Jong-Un'):
        sz.kim.red.on()
        sz.kim.green.off()
    else:
        sz.kim.green.on()
        sz.kim.red.off()

    if in_the_news('Theresa May'):
        sz.may.red.on()
        sz.may.green.off()
    else:
        sz.may.green.on()
        sz.may.red.off()

    sleep(60*60)  # check every hour
