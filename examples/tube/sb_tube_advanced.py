from tubestatus import Status
from gpiozero import StatusBoard
from time import sleep

tube = Status()
lines = ['Central', 'Northern', 'Piccadilly']

sz = StatusBoard()

while True:
    for strip, line in zip(sz, lines):
        status = tube.get_status(line)
        {
            'Good Service': strip.green.on,
            'Minor Delays': strip.green.blink,
            'Severe Delays': strip.red.on,
            'Part Closure': strip.red.blink,
            'Service Closed': strip.off,
        }[status.description]()
    sleep(60)  # check every minute
