from tubestatus import Status
from gpiozero import StatusZero
from time import sleep

tube = Status()
lines = ['Central', 'Northern', 'Piccadilly']

sz = StatusZero()

while True:
    for i, line in enumerate(lines):
        strip = sz[i]
        status = tube.get_status(line)
        action = {
            'Good Service': strip.green.on,
            'Minor Delays': strip.green.blink,
            'Severe Delays': strip.red.on,
            'Part Closure': strip.red.blink,
            'Service Closed': strip.off,
        }[status.description]
        strip.off()
        action()
    sleep(60)
