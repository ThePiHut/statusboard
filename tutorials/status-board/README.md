# STATUS Board tutorial

STATUS Board comprises five strips, each containing a button (available separately) and a pair of LEDS
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
sb.two.lights.green.on()  # green led of second strip on
sleep(1)
sb.two.lights.red.blink()  # blink red led of second strip
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

## Test the LEDs

A simple example to check all your LEDs are working. Try opening a Python shell
and typing these commands (you don't need to type the # comments):

```python
>>> from gpiozero import StatusBoard
>>> sb = StatusBoard()
>>> sb.one.lights.on()  # both lights on the first strip should come on
>>> sb.two.lights.green.on()  # the green light on the second strip should come on
>>> sb.two.lights.red.on()  # the red light on the second strip should come on
>>> sb.three.lights.blink()  # both lights on the third strip should blink
>>> for strip in sb:
...     strip.lights.on()  # all lights should come on
```

## Test the buttons

A simple example to check all your buttons are working:

```python
>>> from gpiozero import StatusBoard
>>> sb = StatusBoard()
>>> for n, strip in enumerate(sb, 1):
...     strip.button.when_pressed = lambda: print('button {} pressed'.format(n))
```

A simple example to test toggling the lights when buttons are pressed:

```python
>>> from gpiozero import StatusBoard
>>> sb = StatusBoard()
>>> for n, strip in sb:
...     strip.lights.red.on()
...     strip.button.when_pressed = strip.lights.toggle
```

## Project

The project: use two strips of the Status Board to indicate the status of the
local network, and of the internet connection. Green means online and red means
offline.

The `PingServer` class from GPIO Zero provides a familiar interface to checking
network connections. You can use it to check whether an IP address on your local
network is reachable or check your connection to the internet.

Try using `PingServer` on its own in a Python shell:

```python
>>> from gpiozero import PingServer
>>> google = PingServer('google.com')
>>> google.is_active  # should print True if you are online
```

Now open a new file and type the following script:

```python
from gpiozero import PingServer, StatusBoard
from time import sleep

google = PingServer('google.com')
sb = StatusBoard('google')

while True:
    if google.is_active:
        sb.google.lights.green.on()
        sb.google.lights.red.off()
    else:
        sb.google.lights.green.off()
        sb.google.lights.red.on()
    sleep(60)
```

Here we use a `while` loop to keep checking the status of the `google.com` ping
every 60 seconds. If it's active, we turn the green LED on and the red off. If
it's inactive, we turn the green off and the red on.

If you wanted to monitor a second server alongside this, you could just add in
another `PingServer` instance and add the same logic into the `while` loop.
You'd also add a second named strip to the `StatusBoard`. For example if
`192.168.1.1` is the IP address of your home router, you could ping it to see if
your local network is reachable:

```python
from gpiozero import PingServer, StatusBoard
from time import sleep

router = PingServer('192.168.1.1')
google = PingServer('google.com')

sb = StatusBoard('router', 'google')

while True:
    if router.is_active:
        sb.router.lights.green.on()
        sb.router.lights.red.off()
    else:
        sb.router.lights.green.off()
        sb.router.lights.red.on()
    if google.is_active:
        sb.google.lights.green.on()
        sb.google.lights.red.off()
    else:
        sb.google.lights.green.off()
        sb.google.lights.red.on()
    sleep(60)
```

Another way of controlling the LEDs is by setting the value of a LED strip. Each
LED strip's value is a 2-tuple, e.g. `(True, True)` when they're both on. `0`
and `1` work as values too.

```python
from gpiozero import PingServer, StatusBoard
from time import sleep

router = PingServer('192.168.1.1')
google = PingServer('google.com')

sb = StatusBoard('router', 'google')

while True:
    if router.is_active:
        sb.router.lights.value = (0, 1)
    else:
        sb.router.lights.value = (1, 0)
    if google.is_active:
        sb.google.lights.value = (0, 1)
    else:
        sb.google.lights.value = (1, 0)
    sleep(60)
```

This example uses the same while loop but rather than individually turning each
LED on and off, the board's value is set to `(1, 0)` (red on, green off) or
`(0, 1)` (red off, green on) which is more concise and uses fewer lines of code.

Rather than use a while loop to continuously set a device's value, you can use a
more advanced approach, connecting an LED with a stream of values.

```python
from gpiozero import PingServer, StatusBoard
from signal import pause

sb = StatusBoard('router', 'google')

router = PingServer('192.168.1.1')
google = PingServer('google.com')

sb.router.lights.green.source = router.values
sb.router.lights.green.source_delay = 60
sb.router.lights.red.source = negated(sb.router.lights.green.values)

sb.google.lights.green.source = google.values
sb.google.lights.green.source_delay = 60
sb.google.lights.red.source = negated(sb.google.lights.green.values)

pause()
```

Instead of a while loop, the status of the green LED is set to follow the status
of the ping server, and the red LED is set to be the opposite of the green LED.
No loop is needed as this happens in the background, but `pause()` is required
to keep the script running.

Rather than repeating the code which sets up the green and red LEDs for each
indicator, a dictionary is formed mapping each ping server to a status strip and
the LED behaviour setup is in a loop.

```python
from gpiozero import PingServer, StatusBoard
from signal import pause

sb = StatusBoard('router', 'google')

statuses = {
    sb.router: PingServer('192.168.1.1'),
    sb.google: PingServer('google.com'),
}

for server, strip in statuses.items():
    strip.lights.green.source = server.values
    strip.lights.green.source_delay = 60
    strip.lights.red.source = negated(strip.lights.green.values)

pause()
```

## More

You can use almost anything as the "input" for your STATUS indicator. If it's
another GPIO Zero device, like a sensor or one of the internal devices like
above, that's easy because they're made to be connected up. If it's something
else entirely, all you have to do is write a function which calculates a True or
False value to send to the LEDs.

For example, use `requests` to get the content from the BBC News homepage, and
check to see if the text contains any particular names (in case you want to
avoid it!):

```python
def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    r = requests.get(url)
    return text in r.text
```

This function returns `True` if the term passed in can be found in the web
request, and `False` if not. Therefore `if in_the_news('Donald Trump')` would
pass if Donald Trump was in the news, and would go to the `else` if not.

The example in full:

```python
from gpiozero import StatusBoard
import requests
from time import sleep

def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    r = requests.get(url)
    return text in r.text

sb = StatusBoard()

while True:
    if in_the_news('Donald Trump'):
        sb.one.lights.red.on()
        sb.one.lights.green.off()
    else:
        sb.one.lights.green.on()
        sb.one.lights.red.on()
    sleep(60*60)  # check every hour

```

Alternatively, using the source/values technique, the function would contain a
`while True` and would `yield` the value each time, checking at an interval
determined by the `source_delay`.

```python
def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    while True:
        r = requests.get(url)
        yield text in r.text
```

And in full:

```python
from gpiozero import StatusBoard
from gpiozero.tools import negated
import requests
from signal import pause

def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    while True:
        r = requests.get(url)
        yield text in r.text

sb = StatusBoard()

sb.one.lights.red.source = in_the_news('Donald Trump')
sb.one.lights.red.source_delay = 60  # check every hour
sb.one.lights.green.source = negated(sb.one.lights.red.values)

pause()
```

## Use button for update

One use of the buttons could be to prompt the status lights to update:

```python
from gpiozero import PingServer, StatusBoard
from signal import pause

sb = StatusBoard('google')

google = PingServer('google.com')

def update():
    if google.is_active:
        sb.google.lights.green.on()
        sb.google.lights.red.off()
    else:
        sb.google.lights.red.on()
        sb.google.lights.green.off()

sb.google.button.when_pressed = update

pause()
```

And to have it auto-update every minute, but also when pressed:

```python
from gpiozero import PingServer, StatusBoard
from time import sleep

sb = StatusBoard('google')

google = PingServer('google.com')

def update():
    if google.is_active:
        sb.google.lights.green.on()
        sb.google.lights.red.off()
    else:
        sb.google.lights.red.on()
        sb.google.lights.green.off()

sb.google.button.when_pressed = update

while True:
    update()
```

or using the source/values approach:

```python
from gpiozero import PingServer, StatusBoard
from signal import pause

sb = StatusBoard('google')

google = PingServer('google.com')

def update():
    sb.google.lights.green.value = google.value

sb.google.lights.green.source = google.values
sb.google.lights.green.source_delay = 60
sb.google.lights.red.source = negated(sb.google.lights.green.values)
sb.google.button.when_pressed = update

pause()
```

## Examples

Next, check out some [examples](../../examples/README.md)
