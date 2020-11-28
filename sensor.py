import pyb
import machine
import onewire
import ds18x20


def get_sensor():
    ds_pin = machine.Pin('PD11')
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
    roms = ds_sensor.scan()
    return roms, ds_sensor


def get_info():
    ds_pin = machine.Pin('PD11')
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

    roms = ds_sensor.scan()
    print('Found DS devices:', roms)

    if not len(roms):
        print('There are no DS devices to read from')


def show_from_all_roms():
    roms, ds_sensor = get_sensor()
    ds_sensor.convert_temp()
    for rom in roms:
        pyb.delay(250)
        print(rom)
        print(ds_sensor.read_temp(rom))


def get_temp(rom_index):
    roms, ds_sensor = get_sensor()
    if len(roms) > rom_index:
        ds_sensor.convert_temp()
        return ds_sensor.read_temp(roms[rom_index])
    else:
        get_info()
        print("Can't find device with index", rom_index)
        return None
