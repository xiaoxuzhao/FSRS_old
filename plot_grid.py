# -*- coding: utf-8 -*-
"""
plot grid
Created on Mon Mar 19 10:38:34 2018

@author: xiaoxu Zhao
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import copy
from pandas import read_csv
from matplotlib.patches import Polygon
#####################
#HARDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
#####################
dfGrid=read_csv(input_dir+'GridPolys.csv')
PID=dfGrid['PID']
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
###########
#remove duplicate elements from the list
S=[]
for a in SID:
    if a not in S:
        S.append(a)
###########
#SID="348" plot lines
s,d=0,0
for i in range(len(SID)):
       if S[s]==SID[i]:
           d+=1
my_map.plot(x[s:s+d],y[s:s+d], '-', markersize=10, linewidth=2, color='r', markerfacecolor='b')
###############
c=0
for s in range(1,len(S)):
    c+=d
    d=0
    for i in range(len(SID)):
       if S[s]==SID[i]:
           d+=1
    my_map.plot(x[c:c+d],y[c:c+d], '-', markersize=10, linewidth=2, color='r', markerfacecolor='b')
##################
my_map.drawcoastlines() 
plt.title('Lobster Fishing areas',fontsize=20) 
my_map.drawparallels(np.arange(40,80,3),labels=[1,0,0,0])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig(save_dir+'lobster_fishing_areas)',dpi=200) 
plt.show()
