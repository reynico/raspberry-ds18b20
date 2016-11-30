#!/usr/bin/python2
import sqlite3 as lite
import datetime
import glob
import time
import sys
import os

#Conectamos a la DB
con = lite.connect('/mnt/InSync/temperature.db')

#Modulos de 1-Wire
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#Conectamos el sensor
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#Raw temp
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
        temp_c = float(temp_string) / 1000.0
        #Not even the best solution, but seems the DS18B20 reads 3* upper than the real
        return temp_c - 3



place = "Living"
with con:
    cur = con.cursor()
    cur.execute("insert into temperature values (NULL,'%s','%s','%s')" % (place, read_temp(), datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    con.commit()
con.close()
