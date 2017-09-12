from gpiozero import StatusBoard
import requests
from time import sleep

def website_up(url):
    try:
        r = requests.get(url)
        return r.ok
    except:
        return False

sb = StatusBoard('raspberrypi', 'codeclub', 'coderdojo')

while True:
    if website_up('https://www.google.com/'):
        if website_up('https://www.raspberrypi.org/'):
            sb.raspberrypi.lights.green.on()
            sb.raspberrypi.lights.red.off()
        else:
            sb.raspberrypi.lights.red.on()
            sb.raspberrypi.lights.green.off()

        if website_up('https://www.codeclub.org.uk/'):
            sb.codeclub.lights.green.on()
            sb.codeclub.lights.red.off()
        else:
            sb.codeclub.lights.red.on()
            sb.codeclub.lights.green.off()

        if website_up('https://www.coderdojo.com/'):
            sb.coderdojo.lights.green.on()
            sb.coderdojo.lights.red.off()
        else:
            sb.coderdojo.lights.red.on()
            sb.coderdojo.lights.green.off()
    else:
        for strip in sz:
            strip.lights.blink()  # internet down, blink everything

    sleep(60*60)  # check every hour
