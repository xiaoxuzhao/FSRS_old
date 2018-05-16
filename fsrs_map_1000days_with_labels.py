# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:18:01 2018

@author: xiaoxu
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
#####################
#HARDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
df_fsrs_1000=read_csv(input_dir+'fsrs_sites(>1000days).csv')   #fsrs_sites(>some days).py
index_1000=list(df_fsrs_1000.icol(0))
fig = plt.figure()
a=fig.add_subplot(1,1,1)
my_map = Basemap(projection='merc', lat_0 = 43, lon_0 = -64,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-66.5, llcrnrlat=42.9,
    urcrnrlon=-63, urcrnrlat=45.1) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'w')
my_map.drawmapboundary()
x,y=my_map(df_fsrs_1000['Longitude'].values,df_fsrs_1000['Latitude'].values)
for i in range(len(x)):
    plt.text(x[i], y[i],index_1000[i],fontsize=10,fontweight='bold', ha='left',va='top',color='r')
my_map.plot(x, y, 'bo', markersize=10)
a.set_title('Longterm sites (>1000 days)',fontsize=20)
my_map.drawparallels(np.arange(40,80,3),labels=[1,0,0,1])
my_map.drawmeridians(np.arange(-180,180,3),labels=[1,1,0,1])
plt.savefig(save_dir+'compare_getfsrs_map_1000_days',dpi=200) 
plt.show()
#