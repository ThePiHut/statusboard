from travispy import TravisPy
from gpiozero import StatusBoard
from gpiozero.tools import negated
from time import sleep
from signal import pause

def build_passed(repo):
    t = TravisPy()
    r = t.repo(repo)
    while True:
        yield r.last_build_state == 'passed'

sb = StatusBoard()

repos = ['RPi-Distro/python-gpiozero', 'raspberrypi/documentation']

for strip, repo in zip(sb, repos):
	strip.lights.green.source = build_passed(repo)
    strip.lights.green.source_delay = 60 * 5  # check every 5 minutes
	strip.lights.red.source = negated(strip.lights.green.values)

pause()
