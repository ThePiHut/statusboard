from gpiozero import StatusZero
import requests
from time import sleep

def website_up(url):
    try:
        r = requests.get(url)
        return r.ok
    except:
        return False

sz = StatusZero('raspberrypi', 'codeclub', 'coderdojo')

while True:
    if website_up('https://www.google.com/'):
        if website_up('https://www.raspberrypi.org/'):
            sz.raspberrypi.red.on()
            sz.raspberrypi.green.off()
        else:
            sz.raspberrypi.green.on()
            sz.raspberrypi.red.on()

        if website_up('https://www.codeclub.org.uk/'):
            sz.codeclub.red.on()
            sz.codeclub.green.off()
        else:
            sz.codeclub.green.on()
            sz.codeclub.red.on()

        if website_up('https://www.coderdojo.com/'):
            sz.coderdojo.red.on()
            sz.coderdojo.green.off()
        else:
            sz.coderdojo.green.on()
            sz.coderdojo.red.on()
    else:
        sz.blink()  # internet down, blink everything

    sleep(60*60)  # check every hour
