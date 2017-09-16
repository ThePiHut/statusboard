from gpiozero import StatusZero
from speedtest import Speedtest
from time import sleep

sb = StatusZero()

st = Speedtest()

def update():
    while True:
        st.get_best_server()

        down = st.download()
        up = st.upload()

        yield (
            (None, (up > 1000000, down > 1000000)),
            (None, (up > 3000000, down > 3000000)),
            (None, (up > 5000000, down > 5000000)),
            (None, (up > 7000000, down > 7000000)),
            (None, (up > 9000000, down > 9000000)),
        )

sb.source = update()
sb.source_delay = 60*10  # check every 10 minutes

while True:
    print(tuple(sb.value))
    sleep(1)
