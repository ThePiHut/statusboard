from gpiozero import StatusZero, PingServer
from gpiozero.tools import negated, smoothed
from signal import pause

sz = StatusZero('mum', 'dad', 'alice')

statuses = {
    PingServer('192.168.1.5'): sz.mum,
    PingServer('192.168.1.6'): sz.dad,
    PingServer('192.168.1.7'): sz.alice,
}

for server, strip in statuses.items():
    strip.green.source = smoothed(server.values, 2, any)  # allow 1 false negative out of 2
    strip.green.source_delay = 60
    strip.red.source = negated(strip.green.values)

pause()
