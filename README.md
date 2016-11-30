Raspberry PI and DS18B20 digital sensor graphing tool
=====================================================
Simple Python code to read, store and plot a DS18B20 temperature sensor. Temps are stored on a SQLite3 database and plotted to a graph using matplotlib.

![alt_text](https://github.com/reynico/raspberry-ds18b20/raw/master/Living-temperature-last-day.png "Temperatures last day")

Requisites
----------
* Matplotlib
* SQLite3

Usage
-----
* Connect the DS18B20 as the diagram shows
* Add `dtoverlay=w1-gpio` to /boot/config.txt and reboot your Raspberry PI
* Modprobe the modules
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
```
* Then you can execute the create table query now! Then run temp.py to store your first reading (-:
* Cron temp.py every minute to get a data series about the temperature readings, then you can plot them using plot.py or just check them out running a query on SQLite.

Electric diagram
----------------
* I used GPIO 4 for the sensor reading, you can use any of the GPIO pins available. I've taken the circuit diagram from http://www.reuk.co.uk/wordpress/raspberry-pi/ds18b20-temperature-sensor-with-raspberry-pi/
