from travispy import TravisPy
from gpiozero import StatusZero
from gpiozero.tools import negated
from time import sleep
from signal import pause

def build_passed(repo):
    t = TravisPy()
    r = t.repo(repo)
    while True:
        yield r.last_build_state == 'passed'

sz = StatusZero()

repos = ['RPi-Distro/python-gpiozero', 'raspberrypi/documentation']

for strip, repo in zip(sz, repos):
	strip.green.source = build_passed(repo)
    strip.green.source_delay = 60 * 5  # check every 5 minutes
	strip.red.source = negated(strip.green.values)

pause()
