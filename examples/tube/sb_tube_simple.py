from tubestatus import Status
from gpiozero import StatusBoard
from time import sleep

tube = Status()

sb = StatusBoard('central', 'northern', 'piccadilly')

while True:
    central = tube.get_status('Central')
    sb.central.lights.off()
    if central.description == 'Good Service':
        sb.central.lights.green.on()
    elif central.description == 'Minor Delays':
        sb.central.lights.green.blink()
    elif central.description == 'Severe Delays':
        sb.central.lights.red.on()
    elif central.description == 'Part Closure':
        sb.central.lights.red.blink()
    elif central.description == 'Service Closed':
        sb.central.lights.off()

    northern = tube.get_status('Northern')
    sb.northern.lights.off()
    if northern.description == 'Good Service':
        sb.northern.lights.green.on()
    elif northern.description == 'Minor Delays':
        sb.northern.lights.green.blink()
    elif northern.description == 'Severe Delays':
        sb.northern.lights.red.on()
    elif northern.description == 'Part Closure':
        sb.northern.lights.red.blink()
    elif northern.description == 'Service Closed':
        sb.northern.lights.off()

    piccadilly = tube.get_status('Piccadilly')
    sb.piccadilly.lights.off()
    if piccadilly.description == 'Good Service':
        sb.piccadilly.lights.green.on()
    elif piccadilly.description == 'Minor Delays':
        sb.piccadilly.lights.green.blink()
    elif piccadilly.description == 'Severe Delays':
        sb.piccadilly.lights.red.on()
    elif piccadilly.description == 'Part Closure':
        sb.piccadilly.lights.red.blink()
    elif piccadilly.description == 'Service Closed':
        sb.piccadilly.lights.off()
    sleep(60)  # check every minute
