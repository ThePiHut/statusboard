from gpiozero import StatusBoard, MotionSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.tools import negated
from signal import pause

living_room_pi = PiGPIOFactory(host='192.168.1.3')
dining_room_pi = PiGPIOFactory(host='192.168.1.4')
bedroom_pi = PiGPIOFactory(host='192.168.1.5')

sb = StatusBoard('living_room', 'dining_room', 'bedroom')  # on this pi
living_room = MotionSensor(17, pin_factory=living_room_pi)  # remote sensors
dining_room = MotionSensor(17, pin_factory=dining_room_pi)
bedroom = MotionSensor(17, pin_factory=bedroom_pi)

while True:
    if living_room.motion_detected:
        sb.living_room.lights.green.on()
        sb.living_room.lights.red.off()
    else:
        sb.living_room.lights.red.on()
        sb.living_room.lights.green.off()

    if dining_room.motion_detected:
        sb.dining_room.lights.green.on()
        sb.dining_room.lights.red.off()
    else:
        sb.dining_room.lights.red.on()
        sb.dining_room.lights.green.off()

    if bedroom.motion_detected:
        sb.bedroom.lights.green.on()
        sb.bedroom.lights.red.off()
    else:
        sb.bedroom.lights.red.on()
        sb.bedroom.lights.green.off()

    sleep(5)
