from gpiozero import StatusZero, PingServer
from gpiozero.tools import negated
from signal import pause

sz = StatusZero()

websites = ['raspberrypi.org', 'codeclub.org.uk', 'coderdojo.com']
servers = [PingServer(web) for web in websites]

for strip, server in zip(sz, servers):
	strip.green.source = server.values
	strip.red.source = negated(strip.green.values)

pause()
