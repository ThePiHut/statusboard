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
            sz.raspberrypi.green.on()
            sz.raspberrypi.red.off()
        else:
            sz.raspberrypi.red.on()
            sz.raspberrypi.green.off()

        if website_up('https://www.codeclub.org.uk/'):
            sz.codeclub.green.on()
            sz.codeclub.red.off()
        else:
            sz.codeclub.red.on()
            sz.codeclub.green.off()

        if website_up('https://www.coderdojo.com/'):
            sz.coderdojo.green.on()
            sz.coderdojo.red.off()
        else:
            sz.coderdojo.red.on()
            sz.coderdojo.green.off()
    else:
        sz.blink()  # internet down, blink everything

    sleep(60*60)  # check every hour
