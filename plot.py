#!/usr/bin/python2
from matplotlib import use as mp_use
mp_use('Agg')
from matplotlib.dates import datetime as dt
from matplotlib.dates import DateFormatter
from matplotlib import rcParams as plt_cfg
from matplotlib import pyplot as plt
from matplotlib import use as mpl
from sqlite3 import connect as db
import sys

#DB Connection
con = db ('/mnt/InSync/temperature.db')
cur = con.cursor()

#Set a time range to plot. 60 equals 60 minutes data series.
timerange = sys.argv[2]
#Place where the sensor is. Living was hardcoded on temp.py
place = sys.argv[1]

#Data extraction
datequery = "select Timestamp from temperature where name = '%s' limit '%s' offset (select count(*) from temperature)-'%s'" % (place,timerange,timerange)
tempquery = "select temperature from temperature where name = '%s' limit '%s' offset (select count(*) from temperature)-'%s'" % (place,timerange,timerange)
dates = cur.execute(datequery).fetchall()
temps = cur.execute(tempquery).fetchall()

#Data format
x = []
for item in dates:
	x.extend(item)

y = []
for item in temps:
	y.extend(item)

if timerange == '1440':
    timerange = 'day'

formatter = DateFormatter('%d-%m %H:%M')

f = plt.figure()
ax = f.add_subplot(111)
if timerange == 'day':
    ax.set_title(place + ' temperature last ' + timerange)
else:
    ax.set_title(place + ' temperature last ' + timerange + ' minutes')
plt_cfg.update({'font.size': 10})
x = [dt.datetime.strptime(d,'%Y-%m-%d %H:%M') for d in x]
plt.xticks(rotation=70)
plt.plot(x, y)
#Y axis limit
axes = plt.gca()
axes.set_ylim([(int(min(y))-3),(int(max(y))+1)])
ax.xaxis.set_major_formatter(formatter)
fig = plt.gcf()
fig.subplots_adjust(bottom=0.3)
fig.set_size_inches(10, 4)
if timerange == 'day':
    filename = '/mnt/stats/' + place + '-temperature-last-' + timerange + '.png'
else:
    filename = '/mnt/stats/' + place + '-temperature-last-' + timerange + 'min.png'
fig.savefig(filename, dpi=100)
