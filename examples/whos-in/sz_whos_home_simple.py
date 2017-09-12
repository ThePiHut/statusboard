from gpiozero import StatusZero, PingServer
from time import sleep

sz = StatusZero('mum', 'dad', 'alice')

mum = PingServer('192.168.1.3')
dad = PingServer('192.168.1.4')
alice = PingServer('192.168.1.5')

while True:
    if mum.is_active:
        sz.mum.green.on()
        sz.mum.red.off()
    else:
        sz.mum.red.on()
        sz.mum.green.off()

    if dad.is_active:
        sz.dad.green.on()
        sz.dad.red.off()
    else:
        sz.dad.red.on()
        sz.dad.green.off()

    if alice.is_active:
        sz.alice.green.on()
        sz.alice.red.off()
    else:
        sz.alice.red.on()
        sz.alice.green.off()

    sleep(60)  # check every minute
