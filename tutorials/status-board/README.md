# STATUS Board tutorial

STATUS Zero comprises five strips, each containing a button and a pair of LEDS
(red and green).

## Basic usage

You can control the LEDs on the board individually, in pairs, or all together.
You can also wait for button presses or fire events when buttons are pressed.

```python
from gpiozero import StatusBoard
from time import sleep

sb = StatusBoard()

sb.one.button.wait_for_press()  # wait for the first button to be pressed
sb.on()  # all leds on
sb.one.button.wait_for_release()  # wait for the first button to be released
sleep(1)
sb.off()  # all leds off
sleep(1)
sb.one.on()  # both leds of first strip on
sleep(1)
sb.two.green.on()  # green led of second strip on
sleep(1)
sb.two.red.blink()  # blink red led of second strip
```

### PWM (variable brightness)

As well as on/off you can use PWM (pulse-width modulation) to control the
brightness of the LEDs:

```python
from gpiozero import StatusBoard
from time import sleep

sb = StatusBoard(pwm=True)

sb.on()  # all leds on
sleep(1)
sb.off()  # all leds off
sleep(1)
sb.one.lights.green.value = 0.5  # green led of first strip at half brightness
sleep(1)
sb.two.value = (0.5, 0.5)  # both leds of second strip at half brightness
sleep(1)
sb.one.lights.pulse()  # both leds of first strip fading in and out
sleep(1)
sb.two.lights.pulse()  # both leds of second strip pulsing in opposite timing with the first
```

## Naming strips

If you initialise `StatusBoard` with no positional arguments, the five strips
will be named `one` to `five`. Optionally, you can instead name up to five
strips like so:

```python
from gpiozero import StatusBoard
from time import sleep

sb = StatusBoard('a', 'b', 'c', 'd')  # only using four strips

sb.on()  # all leds on
sleep(1)
sb.off()  # all leds off
sleep(1)
sb.a.on()  # both leds of first strip on
sleep(1)
sb.d.lights.green.on()  # green led of fourth strip on
sleep(1)
```

So if the strips represent different people, you might name the strips for each
person:

```python
sb = StatusBoard('mum', 'dad', 'alice', 'bob')
```

Or if they're monitoring whether it's raining in different cities:

```python
sb = StatusBoard('sheffield', 'nottingham', 'cambridge', 'dundee')
```

You can name up to five strips. Any without names are not used (except when none
are named).

## Continue

Continue on to the simple tutorial (easy to understand for beginners) or the
advanced tutorial, which uses some more advanced programming techniques:

- [Simple tutorial](simple.md)
- [Advanced tutorial](advanced.md)

Or skip straight to the [examples](../../examples/README.md).
