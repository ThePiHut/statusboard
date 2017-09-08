from gpiozero import StatusBoard
import requests
from time import sleep

def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    r = requests.get(url)
    return text in r.text

sb = StatusBoard('trump', 'kim', 'may')

while True:
    if in_the_news('Donald Trump'):
        sb.trump.lights.red.on()
        sb.trump.lights.green.off()
    else:
        sb.trump.lights.green.on()
        sb.trump.lights.red.on()

    if in_the_news('Kim Jong-Un'):
        sb.kim.lights.red.on()
        sb.kim.lights.green.off()
    else:
        sb.kim.lights.green.on()
        sb.kim.lights.red.on()

    if in_the_news('Theresa May'):
        sb.may.lights.red.on()
        sb.may.lights.green.off()
    else:
        sb.may.lights.green.on()
        sb.may.lights.red.on()

    sleep(60*60)  # check every hour
