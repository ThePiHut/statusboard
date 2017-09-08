from tubestatus import Status
from gpiozero import StatusZero
from time import sleep

tube = Status()

sz = StatusZero('central', 'northern', 'piccadilly')

while True:
    central = tube.get_status('Central')
    sz.central.off()
    if central.description == 'Good Service':
        sz.central.green.on()
    elif central.description == 'Minor Delays':
        sz.central.green.blink()
    elif central.description == 'Severe Delays':
        sz.central.red.on()
    elif central.description == 'Part Closure':
        sz.central.red.blink()
    elif central.description == 'Service Closed':
        sz.central.off()

    northern = tube.get_status('Northern')
    sz.northern.off()
    if northern.description == 'Good Service':
        sz.northern.green.on()
    elif northern.description == 'Minor Delays':
        sz.northern.green.blink()
    elif northern.description == 'Severe Delays':
        sz.northern.red.on()
    elif northern.description == 'Part Closure':
        sz.northern.red.blink()
    elif northern.description == 'Service Closed':
        sz.northern.off()

    piccadilly = tube.get_status('Piccadilly')
    sz.piccadilly.off()
    if piccadilly.description == 'Good Service':
        sz.piccadilly.green.on()
    elif piccadilly.description == 'Minor Delays':
        sz.piccadilly.green.blink()
    elif piccadilly.description == 'Severe Delays':
        sz.piccadilly.red.on()
    elif piccadilly.description == 'Part Closure':
        sz.piccadilly.red.blink()
    elif piccadilly.description == 'Service Closed':
        sz.piccadilly.off()
    sleep(60)  # check every minute
