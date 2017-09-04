from gpiozero import StatusBoard
from gpiozero.tools import negated
from signal import pause

sb = StatusBoard()

for strip in sb:
    strip.lights.green.source = strip.button.values
    strip.lights.red.source = negated(strip.button.values)

pause()
