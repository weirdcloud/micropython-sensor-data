# main.py -- put your code here!
import pyb
import json
import micropython

from sensor import get_temp
from sending import send_temp


# minimum / maximum temperature
min_temp = 15
max_temp = 20
# delay between getting temperature
ms_delay = 10000
# index of device to read from
rom_index = 0

# saving objects
led_red = pyb.LED(1)
led_blue = pyb.LED(4)


def make_json(temp):
    data = {
        "temperature": temp,
        "max_temperature": max_temp,
        "min_temperature": min_temp,
    }
    data_json = json.dumps(data)
    return data_json


def update():
    temp = get_temp(rom_index)
    # print("current:", temp, "max:", max_temp, "min:", min_temp)
    if temp is None:
        print("Can't find device to read from")
        return

    temp_json = make_json(temp)
    send_temp(temp_json)

    if temp >= max_temp:
        led_red.on()
    else:
        led_red.off()

    if temp <= min_temp:
        led_blue.on()
    else:
        led_blue.off()


# main loop
while True:
    pyb.delay(ms_delay)
    update()
