from gpiozero import StatusBoard
from speedtest import Speedtest
from time import sleep

sb = StatusBoard()

st = Speedtest()

while True:
    st.get_best_server()

    down = st.download()
    if down > 90000000:  # 90Mb
        sb.one.lights.green.on()
    if down > 70000000:  # 70Mb
        sb.two.lights.green.on()
    if down > 50000000:  # 50Mb
        sb.three.lights.green.on()
    if down > 30000000:  # 30Mb
        sb.four.lights.green.on()
    if down > 10000000:  # 10Mb
        sb.five.lights.green.on()

    up = st.upload()
    if up > 90000000:  # 9Mb
        sb.one.lights.red.on()
    if up > 7000000:  # 7Mb
        sb.two.lights.red.on()
    if up > 5000000:  # 5Mb
        sb.three.lights.red.on()
    if up > 3000000:  # 3Mb
        sb.four.lights.red.on()
    if up > 1000000:  # 1Mb
        sb.five.lights.red.on()

    sleep(60*10)  # check every 10 minutes
