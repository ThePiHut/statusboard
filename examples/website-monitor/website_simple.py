from gpiozero import StatusZero, PingServer
from time import sleep

sz = StatusZero('raspberrypi', 'codeclub', 'coderdojo')

raspberrypi = PingServer('raspberrypi.org')
codeclub = PingServer('codeclub.org.uk')
coderdojo = PingServer('coderdojo.com')

while True:
    if raspberrypi.is_active:
        sz.raspberrypi.green.on()
        sz.raspberrypi.red.on()
    else:
        sz.raspberrypi.red.on()
        sz.raspberrypi.green.off()

    if codeclub.is_active:
        sz.codeclub.green.on()
        sz.codeclub.red.on()
    else:
        sz.codeclub.red.on()
        sz.codeclub.green.off()

    if coderdojo.is_active:
        sz.coderdojo.green.on()
        sz.coderdojo.red.on()
    else:
        sz.coderdojo.red.on()
        sz.coderdojo.green.off()

    sleep(60*5)  # check every 5 minutes
