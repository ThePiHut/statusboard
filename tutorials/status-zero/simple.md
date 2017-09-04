# Simple tutorial for STATUS Zero

A simple example to check all your STATUS board elements are working. Try
opening a Python shell and typing these commands (you don't need to type the #
comments):

```python
>>> from gpiozero import StatusZero
>>> sb = StatusBoard()
>>> sb.on()  # all lights should come on
>>> sb.off()  ## all lights should go off
>>> sb.one.blink()  # the lights on the first strip should blink
>>> for strip in sb:
...     strip.button.when_pressed = strip.lights.on
...     strip.button.when_released = strip.lights.off
```

Now when you press any button, the lights on that strip should come on.

### Project

The project: use two strips of the Status Board to indicate the status of the
local network, and of the internet connection. Green means online and red means
offline.

The `PingServer` class from GPIO Zero provides a familiar interface to checking
network connections. You can use it to check whether an IP address on your local
network is reachable or check a website is up or down.

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
from gpiozero import PingServer, StatusBoard
from time import sleep

router = PingServer('192.168.1.1')
google = PingServer('google.com')

sb = StatusBoard('router', 'google')

while True:
    if router.is_active:
        sb.router.green.on()
        sb.router.red.off()
    else:
        sb.router.green.off()
        sb.router.red.on()
    if google.is_active:
        sb.google.green.on()
        sb.google.red.off()
    else:
        sb.google.green.off()
        sb.google.red.on()
    sleep(60)
```

Another way of controlling the LEDs is by setting the value of a LED strip. Each
LED strip's value is a 2-tuple, e.g. `(True, True)` when they're both on.

```python
from gpiozero import PingServer
from status import StatusBoard
from time import sleep

router = PingServer('192.168.1.1')
google = PingServer('google.com')

sb = StatusBoard('router', 'google')

while True:
    if router.is_active:
        sb.router.value = (0, 1)
    else:
        sb.router.value = (1, 0)
    if google.is_active:
        sb.google.value = (0, 1)
    else:
        sb.google.value = (1, 0)
    sleep(60)
```

This example uses the same while loop but rather than individually turning each
LED on and off, the board's value is set to `(1, 0)` (red on, green off) or
`(0, 1)` (red off, green on) which is more concise and uses fewer lines of code.

1. While loop with individual led control (20 lines)

    This example uses a more advanced approach (source/values) but is still quite simple and concise. Instead of a while loop, the status of the green LED is set to follow the status of the ping server, and the red LED is set to be the opposite of the green LED. No loop is needed as this happens in the background but `pause()` is required to keep the script running.

1. While loop with individual led control (16 lines)

    This example also uses the source/values approach, but rather than repeating the code which sets up the green and red LEDs for each indicator, a dictionary is formed mapping each ping server to a Status Board strip and the LED behaviour setup is in a loop.

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

people = ['Donald Trump', 'Kim Jong-Un', 'Theresa May', 'Boris Johnson']

for i, person in enumerate(people):
    strip = sz[i]
    strip.red.source = in_the_news(person)
    strip.red.source_delay = 60
    strip.green.source = negated(strip.red.values)

pause()
```
