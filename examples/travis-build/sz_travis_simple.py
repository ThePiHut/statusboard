from travispy import TravisPy
from gpiozero import StatusZero
from time import sleep

def build_passed(repo):
    t = TravisPy()
    r = t.repo(repo)
    return r.last_build_state == 'passed'

sz = StatusZero('gpiozero', 'documentation')

while True:
    if build_passed('RPi-Distro/python-gpiozero'):
        sz.gpiozero.green.on()
        sz.gpiozero.red.off()
    else:
        sz.gpiozero.red.on()
        sz.gpiozero.green.off()

    if build_passed('raspberrypi/documentation'):
        sz.documentation.green.on()
        sz.documentation.red.off()
    else:
        sz.documentation.red.on()
        sz.documentation.green.off()

    sleep(60*5)  # check every 5 minutes
