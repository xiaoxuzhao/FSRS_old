# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:38:34 2018

@author: xiaoxu Zhao
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
#####################
#HARDCODES
input_dir='/home/zdong/xiaoxu/Lobster/all files/'
save_dir='/home/zdong/xiaoxu/Lobster/figure/'
#####################
dfGrid=read_csv(input_dir+'GridPolys.csv')
PID=dfGrid['PID']
POS=dfGrid['POS']
SID=dfGrid['SID']
lon=list(dfGrid['X'])
lat=list(dfGrid['Y'])
fig = plt.figure()
a=fig.add_subplot(1,1,1)
my_map = Basemap(projection='gall', lat_0 = 45, lon_0 = -63,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68, llcrnrlat=42.0,
    urcrnrlon=-57.6, urcrnrlat=48) 
my_map.drawcountries()
my_map.fillcontinents(color = 'gray')
my_map.drawmapboundary()
x,y=my_map(dfGrid['X'].values,dfGrid['Y'].values)
my_map.plot(x,y, '-', markersize=10, linewidth=2, color='r', markerfacecolor='b')
my_map.drawcoastlines() 
a.set_title('Lobster Fishing areas',fontsize=10) 
my_map.drawparallels(np.arange(40,80,3),labels=[1,0,0,0])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig(save_dir+'lobster_fishing_areas)',dpi=200) 
plt.show()
