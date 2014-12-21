from django.conf import settings
import os
import glob
import time


if settings.DEV_MODE == False:
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_float = float(temp_string)
        temp_c = float('{0:.2f}'.format(temp_float / 1000.0))
        temp_f = float('{0:.2f}'.format(temp_c * 9.0 / 5.0 + 32.0))
        return temp_c, temp_f


def retrieve_temp():
    if settings.DEV_MODE == True:
        return "dev mode"
    else:
        return read_temp()


#while True:
#    print(read_temp())
#    time.sleep(1)
