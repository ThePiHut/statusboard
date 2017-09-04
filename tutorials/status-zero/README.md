# STATUS Zero tutorial

STATUS Zero comprises three strips, each containing a pair of LEDS (red and
green).

## Basic usage

You can control the LEDs on the board individually, in pairs, or all together:

```python
from gpiozero import StatusZero
from time import sleep

sz = StatusZero()

sz.on()  # all leds on
sleep(1)
sz.off()  # all leds off
sleep(1)
sz.one.on()  # both leds of first strip on
sleep(1)
sz.two.green.on()  # green led of second strip on
sleep(1)
sz.two.red.blink()  # blink red led of second strip
```

### PWM (variable brightness)

As well as on/off you can use PWM (pulse-width modulation) to control the
brightness of the LEDs:

```python
from gpiozero import StatusZero
from time import sleep

sz = StatusZero(pwm=True)

sz.on()  # all leds on
sleep(1)
sz.off()  # all leds off
sleep(1)
sz.one.green.value = 0.5  # green led of first strip at half brightness
sleep(1)
sz.two.value = (0.5, 0.5)  # both leds of second strip at half brightness
sleep(1)
sz.one.pulse()  # both leds of first strip fading in and out
sleep(1)
sz.two.pulse()  # both leds of second strip pulsing in opposite timing with the first
```

## Naming strips

If you initialise `StatusZero` with no positional arguments, the three strips
will be named `one` to `three`. Optionally, you can instead name up to three
strips like so:

```python
from gpiozero import StatusBoard
from time import sleep

sb = StatusBoard('a', 'b')  # only using two strips

sb.on()  # all leds on
sleep(1)
sb.off()  # all leds off
sleep(1)
sb.a.on()  # both leds of first strip on
sleep(1)
sb.b.green.on()  # green led of second strip
sleep(1)
```

So if the strips represent different people, you might name the strips for each
person:

```python
sb = StatusBoard('mum', 'dad', 'alice')
```

Or if they're monitoring whether it's raining in different cities:

```python
sb = StatusBoard('sheffield', 'nottingham', 'cambridge')
```

You can name up to five strips. Any without names are not used (except when none
are named).

## Continue

Continue on to the simple tutorial (easy to understand for beginners) or the
advanced tutorial, which uses some more advanced programming techniques:

- [Simple tutorial](simple.md)
- [Advanced tutorial](advanced.md)

Or skip straight to the [examples](../../examples/README.md).
