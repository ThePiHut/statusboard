from gpiozero import StatusBoard, PingServer
from gpiozero.tools import negated, smoothed
from signal import pause

sb = StatusBoard('mum', 'dad', 'alice')

statuses = {
    PingServer('192.168.1.5'): sb.mum,
    PingServer('192.168.1.6'): sb.dad,
    PingServer('192.168.1.7'): sb.alice,
}

for server, strip in statuses.items():
    strip.lights.green.source = smoothed(server.values, 2, any)  # allow 1 false negative out of 2
    strip.lights.green.source_delay = 60
    strip.lights.red.source = negated(strip.lights.green.values)

pause()
