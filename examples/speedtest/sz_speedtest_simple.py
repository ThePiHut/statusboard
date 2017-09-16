from gpiozero import StatusZero
from speedtest import Speedtest
from time import sleep

sz = StatusZero()

st = Speedtest()

while True:
    st.get_best_server()

    down = st.download()
    if down > 60000000:  # 60Mb
        sz.one.green.on()
    if down > 40000000:  # 40Mb
        sz.two.green.on()
    if down > 20000000:  # 20Mb
        sz.three.green.on()

    up = st.upload()
    if up > 60000000:  # 6Mb
        sz.one.red.on()
    if up > 4000000:  # 4Mb
        sz.two.red.on()
    if up > 2000000:  # 2Mb
        sz.three.red.on()

    sleep(60*10)  # check every 10 minutes
