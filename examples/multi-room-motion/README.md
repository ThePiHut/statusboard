# Multi-room motion sensor

Set up multiple Pis around the house with PIR motion sensors attached and use
the STATUS Zero to show which room has motion so you can tell where people are
in the house.

## Requirements

You'll need a Pi (a Pi Zero W would be ideal) in each room you want to monitor.
Each Pi will need to be on the local network. You'll need a PIR motion sensor
connected to each one, and each Pi will need to be running Raspbian with the
pigpio daemon running. No Python code is required on the remote Pis. See the
[GPIO Zero remote GPIO](http://gpiozero.readthedocs.io/en/stable/remote_gpio.html)
documentation for more information.

## Code

You will need to run the Python code on the Pi with the Status Zero attached.

- STATUS Zero
    - [Simple version](sz_motion_simple.py)
    - [Advanced version](sz_motion_advanced.py)
- STATUS Board
    - [Simple version](sb_motion_simple.py)
    - [Advanced version](sb_motion_advanced.py)
