from gpiozero import StatusBoard, MotionSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.tools import negated
from signal import pause

ips = ['192.168.1.3', '192.168.1.4', '192.168.1.5']
remotes = [PiGPIOFactory(host=ip) for ip in ips]

sb = StatusBoard()  # on this pi
sensors = [MotionSensor(17, pin_factory=r) for r in remotes]  # remote sensors

for strip, sensor in zip(sb, sensors):
    strip.lights.green.source = sensor.values
    strip.lights.green.source_delay = 5  # check every 5 seconds
	strip.lights.red.source = negated(strip.lights.green.values)

pause()
