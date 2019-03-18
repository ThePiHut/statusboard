from gpiozero import StatusBoard
from gpiozero.tools import negated, smoothed
import requests
from time import sleep

sb = StatusBoard('raspberrypi', 'codeclub', 'coderdojo')

def website_up(url):
    while True:
        try:
            r = requests.get(url)
            yield r.ok
        except:
            yield False

statuses = {
    sb.raspberrypi: website_up('https://www.raspberrypi.org/'),
    sb.codeclub: website_up('https://www.codeclub.org.uk/'),
    sb.coderdojo: website_up('https://www.coderdojo.com/'),
}

for strip, website in statuses.items():
    strip.lights.green.source = smoothed(website, 2, any)  # allow 1 false negative out of 2
    strip.lights.green.source_delay = 60
    strip.lights.red.source = negated(strip.lights.green.values)
    strip.lights.red.source_delay = 60

google = website_up('https://www.google.com/')

for google_up in google:
    if not google_up:
        for strip in sb:
            strip.lights.blink()
    sleep(60)
