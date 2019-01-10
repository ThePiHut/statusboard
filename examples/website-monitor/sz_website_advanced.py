from gpiozero import StatusZero
from gpiozero.tools import negated, smoothed
import requests
from time import sleep

sz = StatusZero('raspberrypi', 'codeclub', 'coderdojo')

def website_up(url):
    while True:
        try:
            r = requests.get(url)
            yield r.ok
        except:
            yield False

statuses = {
    sz.raspberrypi: website_up('https://www.raspberrypi.org/'),
    sz.codeclub: website_up('https://www.codeclub.org.uk/'),
    sz.coderdojo: website_up('https://www.coderdojo.com/'),
}

for strip, website in statuses.items():
    strip.green.source = smoothed(website, 2, any)  # allow 1 false negative out of 2
    strip.green.source_delay = 60
    strip.red.source = negated(strip.green.values)
    strip.red.source_delay = 60

google = website_up('https://www.google.com/')

for google_up in google:
    if not google_up:
        sz.blink()
    sleep(60)
