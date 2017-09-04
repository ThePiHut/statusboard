from gpiozero import StatusZero, MotionSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.tools import negated
from signal import pause

living_room_pi = PiGPIOFactory(host='192.168.1.3')
dining_room_pi = PiGPIOFactory(host='192.168.1.4')
bedroom_pi = PiGPIOFactory(host='192.168.1.5')

sz = StatusZero('living_room', 'dining_room', 'bedroom')  # on this pi
living_room = MotionSensor(17, pin_factory=living_room_pi)  # remote sensors
dining_room = MotionSensor(17, pin_factory=dining_room_pi)
bedroom = MotionSensor(17, pin_factory=bedroom_pi)

while True:
    if living_room.motion_detected:
        sz.living_room.green.on()
        sz.living_room.red.off()
    else:
        sz.living_room.red.on()
        sz.living_room.green.off()

    if dining_room.motion_detected:
        sz.dining_room.green.on()
        sz.dining_room.red.off()
    else:
        sz.dining_room.red.on()
        sz.dining_room.green.off()

    if bedroom.motion_detected:
        sz.bedroom.green.on()
        sz.bedroom.red.off()
    else:
        sz.bedroom.red.on()
        sz.bedroom.green.off()

    sleep(5)
