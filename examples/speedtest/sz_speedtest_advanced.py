from gpiozero import StatusZero
from speedtest import Speedtest
from time import sleep

sz = StatusZero()

st = Speedtest()

def update():
    while True:
        st.get_best_server()

        down = st.download()
        up = st.upload()

        yield (
            (up > 2000000, down > 2000000),
            (up > 4000000, down > 4000000),
            (up > 6000000, down > 6000000),
        )

sz.source = update()
sz.source_delay = 60*10  # check every 10 minutes

while True:
    print(tuple(sz.value))
    sleep(1)
