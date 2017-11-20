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
from gpiozero import StatusZero
from time import sleep

sz = StatusZero('a', 'b')  # only using two strips

sz.on()  # all leds on
sleep(1)
sz.off()  # all leds off
sleep(1)
sz.a.on()  # both leds of first strip on
sleep(1)
sz.b.green.on()  # green led of second strip
sleep(1)
```

So if the strips represent different people, you might name the strips for each
person:

```python
sz = StatusZero('mum', 'dad', 'alice')
```

Or if they're monitoring whether it's raining in different cities:

```python
sz = StatusZero('sheffield', 'nottingham', 'cambridge')
```

You can name up to three strips. Any without names are not used (except when
none are named).

## Test the LEDs

A simple example to check all your LEDs are working. Try opening a Python shell
and typing these commands (you don't need to type the # comments):

```python
>>> from gpiozero import StatusZero
>>> sz = StatusZero()
>>> sz.on()  # all lights should come on
>>> sz.off()  ## all lights should go off
>>> sz.one.on()  # both lights on the first strip should come on
>>> sz.two.green.on()  # the green light on the second strip should come on
>>> sz.two.red.on()  # the red light on the second strip should come on
>>> sz.three.blink()  # both lights on the third strip should blink
```

## Project

The project: use two strips of the Status Zero to indicate the status of the
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
from gpiozero import PingServer, StatusZero
from time import sleep

google = PingServer('google.com')
sb = StatusZero('google')

while True:
    if google.is_active:
        sb.google.green.on()
        sb.google.red.off()
    else:
        sb.google.green.off()
        sb.google.red.on()
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
from gpiozero import PingServer, StatusZero
from time import sleep

router = PingServer('192.168.1.1')
google = PingServer('google.com')

sz = StatusZero('router', 'google')

while True:
    if router.is_active:
        sz.router.green.on()
        sz.router.red.off()
    else:
        sz.router.green.off()
        sz.router.red.on()
    if google.is_active:
        sz.google.green.on()
        sz.google.red.off()
    else:
        sz.google.green.off()
        sz.google.red.on()
    sleep(60)
```

Another way of controlling the LEDs is by setting the value of a LED strip. Each
LED strip's value is a 2-tuple, e.g. `(True, True)` when they're both on. `0`
and `1` work as values too.

```python
from gpiozero import PingServer, StatusZero
from time import sleep

router = PingServer('192.168.1.1')
google = PingServer('google.com')

sz = StatusZero('router', 'google')

while True:
    if router.is_active:
        sz.router.value = (0, 1)
    else:
        sz.router.value = (1, 0)
    if google.is_active:
        sz.google.value = (0, 1)
    else:
        sz.google.value = (1, 0)
    sleep(60)
```

This example uses the same while loop but rather than individually turning each
LED on and off, the board's value is set to `(1, 0)` (red on, green off) or
`(0, 1)` (red off, green on) which is more concise and uses fewer lines of code.

Rather than use a while loop to continuously set a device's value, you can use a
more advanced approach, connecting an LED with a stream of values.

```python
from gpiozero import PingServer, StatusZero
from signal import pause

sz = StatusZero('router', 'google')

router = PingServer('192.168.1.1')
google = PingServer('google.com')

sz.router.green.source = router.values
sz.router.green.source_delay = 60
sz.router.red.source = negated(sz.router.green.values)

sz.google.green.source = google.values
sz.google.green.source_delay = 60
sz.google.red.source = negated(sz.google.green.values)

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
from gpiozero import PingServer, StatusZero
from signal import pause

sz = StatusZero('router', 'google')

statuses = {
    sz.router: PingServer('192.168.1.1'),
    sz.google: PingServer('google.com'),
}

for server, strip in statuses.items():
    strip.green.source = server.values
    strip.green.source_delay = 60
    strip.red.source = negated(strip.green.values)

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
from gpiozero import StatusZero
import requests
from time import sleep

def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    r = requests.get(url)
    return text in r.text

sz = StatusZero()

while True:
    if in_the_news('Donald Trump'):
        sz.one.red.on()
        sz.one.green.off()
    else:
        sz.one.green.on()
        sz.one.red.on()
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
from gpiozero import StatusZero
from gpiozero.tools import negated
import requests
from signal import pause

def in_the_news(text):
    url = 'http://www.bbc.co.uk/news'
    while True:
        r = requests.get(url)
        yield text in r.text

sz = StatusZero()

sz.one.red.source = in_the_news('Donald Trump')
sz.one.red.source_delay = 60  # check every hour
sz.one.green.source = negated(sz.one.red.values)

pause()
```

## Examples

Next, check out some [examples](../../examples/README.md)
