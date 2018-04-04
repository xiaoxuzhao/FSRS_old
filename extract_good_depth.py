
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:22:21 2018
extract good depth   2890 1779   2890 2025
@author: xiaoxu
"""
from pandas import read_csv
import numpy as np
from pandas import DataFrame
#####################
#HARDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
#####################
def list_of_groups(init_list, childern_list_len):
    #divided the big list into small list
    list_of_groups = zip(*(iter(init_list),) *childern_list_len) 
    end_list = [list(i) for i in list_of_groups] 
    count = len(init_list) % childern_list_len 
    end_list.append(init_list[-count:]) if count !=0 else end_list 
    return end_list
dfh=read_csv(input_dir+'merge_date.csv')
index=dfh.icol(0)
depth=dfh["Depth"]
event_spev=dfh["Event_spec"]
index_sites=dfh['index_sites']
lon=dfh['Longitude']
lat=dfh["Latitude"]
Date=dfh['Date']
Min_temp=dfh['Min_temp']
Max_temp=dfh['Max_temp']
Mean_temp=dfh['Mean_temp']
Stdev_temp=dfh['Stdev_temp']
a,count=[],[]
for i in index:
    if i not in a:
        a.append(i)
for i in range(len(a)):#len(a)
    c=0
    for s in range(len(index)):
        if a[i]==index[s]:
            c+=1
    count.append(c)
dep=0
depp,ind=[],[]
for i in range(count[0]):
    dep+=depth[i]
    depp.append(depth[i])
mdepth=dep/count[0]
for i in range(count[0]):
    if abs(depth[i]-mdepth)<np.std(depp):
          ind.append(i)
d=count[0]

for s in range(1,len(a)):#1:len(a)
    dep=0
    depp=[]
    d+=count[s]
    for i in range(d-count[s],d):
            dep+=depth[i]
            depp.append(depth[i])
    mdepth=dep/count[s]
    for i in range(d-count[s],d):
         if abs(depth[i]-mdepth)<=np.std(depp,ddof=1):
                 ind.append(i)
index_ff=index.loc[ind]
dep=depth.loc[ind]
index_s=index_sites.loc[ind]
Event=event_spev.loc[ind]
lati=lat.loc[ind]
long=lon.loc[ind]
Date=Date.loc[ind]
Dep=depth.loc[ind]
Min_t=Min_temp.loc[ind]
Max_t=Max_temp.loc[ind]
Mean_t=Mean_temp.loc[ind]
Stdev_t=Stdev_temp.loc[ind]
data={'index_sites':np.array(index_s),'Event_spec':np.array(Event),'Latitude':np.array(lati),
      'Longitude':np.array(long),'Date':np.array(Date),'Depth':np.array(Dep),
      'Min_temp':np.array(Min_t),'Max_temp':np.array(Max_t),'Mean_temp':np.array(Mean_t),
      'Stdev_temp':np.array(Stdev_t)}
frame=DataFrame(data,columns=['index_sites','Event_spec','Latitude','Longitude','Date',
                              'Depth','Min_temp','Max_temp','Mean_temp',
                              'Stdev_temp'],index=index_ff)
                              
frame.to_csv(input_dir+"merge_date_good_depth.csv")    
     
         