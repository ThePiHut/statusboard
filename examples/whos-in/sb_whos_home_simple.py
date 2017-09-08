from gpiozero import StatusBoard, PingServer
from time import sleep

sb = StatusBoard('mum', 'dad', 'alice')

mum = PingServer('192.168.1.3')
dad = PingServer('192.168.1.4')
alice = PingServer('192.168.1.5')

while True:
    if mum.is_active:
        sb.mum.lights.green.on()
        sb.mum.lights.red.on()
    else:
        sb.mum.lights.red.on()
        sb.mum.lights.green.off()

    if dad.is_active:
        sb.dad.lights.green.on()
        sb.dad.lights.red.on()
    else:
        sb.dad.lights.red.on()
        sb.dad.lights.green.off()

    if alice.is_active:
        sb.alice.lights.green.on()
        sb.alice.lights.red.on()
    else:
        sb.alice.lights.red.on()
        sb.alice.lights.green.off()

    sleep(60)  # check every minute
