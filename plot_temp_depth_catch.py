# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:03:09 2018

@author: zdong
"""

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
from pandas import read_csv
from dateutil import parser
import numpy as np
import re
from pandas import DataFrame
import pandas as pd
#####################
#HARDCODES
input_dir='C:/Users/11307/Documents/python/getfsrs/all files/'
save_dir='C:/Users/11307/Documents/python/getfsrs/pictures/'
#input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
#save_dir='/home/zdong/xiaoxu/FSRS/figure/'
s=5
index_mt3=[1,16,73,97,145,216,250,329,369,418]
#####################
df=read_csv(input_dir+'355c0671cde98eb5386b570c663fc7327e374d77.csv')
dfh=read_csv(input_dir+'fsrs_sites(1000days).csv')
lat=dfh["Latitude"]
lon=dfh["Longitude"]
Lat=df["decimalLatitude"]
Lon=df["decimalLongitude"]
dep=df["depth"]
Date=df["eventDate"]
info=df["dynamicProperties"]
count=df["individualCount"]
temp=[str(i)[36:62] for i in info]
a=[re.findall(r"[-+]?\d*\.\d+|\d+", i) for i in temp]
b=[str(i) for i in a]
lat=[round(i,2) for i in lat]
lon=[round(i,2) for i in lon]
c=[]
s=3
for i in range(len(Lat)):
    if lat[s]==Lat[i] and lon[s]==Lon[i]:
        c.append(i)
latitude,longitude,depth,tem,catch,date=[],[],[],[],[],[]
c=c[0:5]+c[9:-4]
for s in c:
    latitude.append(Lat[s])
    longitude.append(Lon[s])
    depth.append(dep[s])
    tem.append(b[s])
    catch.append(count[s])
    date.append(Date[s])
D=[]
T=[]
for i in date:
          D.append(parser.parse(i))
for i in tem:
    i=i.replace("['","")
    i=i.replace("']","")
    T.append(i)
print T
data={'Latitude':np.array(latitude),
      'Longitude':np.array(longitude),'Date':np.array(date),'Depth':np.array(depth),
      'Bottom temperature':np.array(T),
      'catchcount':np.array(catch)}
frame=DataFrame(data,columns=['Latitude','Longitude','Date',
                              'Depth','Bottom temperature',
                              'catchcount'],index=c)                              
frame.to_csv(input_dir+"site_97_temp_depth.csv")

host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))

par2.axis["right"].toggle(all=True)


host.set_xlabel("Date")
host.set_ylabel("Temperature",color="r")
par1.set_ylabel("Depth",color='g')
par2.set_ylabel("Catch",color='b')

p1, = host.plot(D, T, 'r.',label="Temperature")
p2, = par1.plot(D, depth,'g.', label="Depth")
p3, = par2.plot(D, catch,'b.', label="Catch")
#host.xticks(pd.date_range('2018-01-01','2009-05-1'),rotation=90)
host.set_xticks(['2012','2013','2014'])
#'2004','2005','2006','2007','2008','2009','2010',
host.set_title("the site 97 Temperature ,Depth and catch")

host.legend(loc=9,fontsize=6)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())

plt.savefig(save_dir+"97_site_temperature_depth_catch.png")
plt.show()
