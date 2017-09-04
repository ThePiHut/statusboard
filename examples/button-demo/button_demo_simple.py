from gpiozero import StatusBoard
from signal import pause

sb = StatusBoard()

for strip in sb:
    # start with all the reds on
    strip.lights.red.on()
    # when the button is pressed, toggle the lights
    strip.button.when_pressed = strip.lights.toggle

pause()
