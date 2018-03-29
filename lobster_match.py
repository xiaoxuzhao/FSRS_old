# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:36:53 2018
match temperature and lobster
@author: xiaoxu
"""
from pandas import read_csv
import pandas as pd
#####################
#HARDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
input_d='/home/zdong/xiaoxu/Lobster/all files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
#####################
dfh=read_csv(input_dir+'CTSeventList_4589.txt',skiprows=[0])
df=read_csv(input_d+'355c0671cde98eb5386b570c663fc7327e374d77.csv')
lat=dfh['Latitude']
lon=dfh['Longitude'] 
lat=[round(i,2) for i in lat]
lon=[round(i,2) for i in lon]
Lon=df['decimalLongitude']
Lat=df['decimalLatitude']
index=[]
for i in range(len(Lat)):
    a=0
    for s in range(len(lat)):
         if Lat[i]==lat[s] and Lon[i]==lon[s]:
             print s
             a=s
             index.append(int(s))
    if a==0:
        index.append(None)
print index
index=pd.Series(index)
df['index'] = index
df.to_csv(input_d+'lobster_match.csv')
