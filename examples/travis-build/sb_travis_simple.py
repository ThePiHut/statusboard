from travispy import TravisPy
from gpiozero import StatusBoard
from time import sleep

def build_passed(repo):
    t = TravisPy()
    r = t.repo(repo)
    return r.last_build_state == 'passed'

sb = StatusBoard('gpiozero', 'documentation')

while True:
    if build_passed('RPi-Distro/python-gpiozero'):
        sb.gpiozero.lights.green.on()
        sb.gpiozero.lights.red.on()
    else:
        sb.gpiozero.lights.red.on()
        sb.gpiozero.lights.green.off()

    if build_passed('raspberrypi/documentation'):
        sb.documentation.lights.green.on()
        sb.documentation.lights.red.on()
    else:
        sb.documentation.lights.red.on()
        sb.documentation.lights.green.off()

    sleep(60*5)  # check every 5 minutes
