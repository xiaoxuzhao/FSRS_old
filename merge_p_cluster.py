# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:26:37 2018

@author: xiaoxu
"""
# -*- coding: utf-8 -*-
from pandas import read_csv
import operator
import numpy as np
from pandas import DataFrame
#################
#HARDCODES
input_dir="/home/zdong/xiaoxu/FSRS/all_files/"
#################
df_sites=read_csv(input_dir+'p_cluster_sites(>1 km,year).csv') #
df_fsrs=read_csv(input_dir+'p_cluster_stations_60.0_bins(fsrs).csv')
df_scalar=read_csv(input_dir+'CTSscalarstats.csv')
def list_of_groups(init_list, childern_list_len):
    #divided the big list into small list
    list_of_groups = zip(*(iter(init_list),) *childern_list_len) 
    end_list = [list(i) for i in list_of_groups] 
    count = len(init_list) % childern_list_len 
    end_list.append(init_list[-count:]) if count !=0 else end_list 
    return end_list
#######################
#make a list of  the whole indexs from the fsrs_sites.csv (2127)
indexs=df_sites["indexs"]
indexs=list(indexs)
index_site=reduce(operator.concat, indexs)
index_site=index_site.replace("][",", ")
index_site=index_site.replace("[","")
index_site=index_site.replace("]","")
index_site=index_site.replace(",","")
index_site=index_site.split() 
index_site=[int(i) for i in index_site]
#######################
event_spec=df_fsrs["Event_Spec"]
lat=df_fsrs["Latitude"]
lon=df_fsrs["Longitude"]
start=df_fsrs["Start"]
event_spec_scalar=df_scalar["Event_Spec"]
lat_scalar=df_scalar["Latitude"]
lon_scalar=df_scalar["Longitude"]
start_scalar=df_scalar["Start"]
end_scalar=df_scalar["End"]
dep=df_scalar["Obs_Dep"]
min_t=df_scalar["Min"]
max_t=df_scalar["Max"]
mean_t=df_scalar["Mean"]
stdev_t=df_scalar["Stdev"]
num_row_near=df_sites["num_row_near"]
Event_spec,Date,num_date,Dep=[],[],[],[]
Min_t,Max_t,Mean_t,Stdev_t,Index_first=[],[],[],[],[]
Lat,Lon=[],[]
for i in index_site:#index_site
    print i
    Event_spec.append(event_spec[i])
    date,num=[],[]
    for s in df_scalar.index:
             if event_spec[i]==event_spec_scalar[s]:
                Lat.append(lat_scalar[s])
                Lon.append(lon_scalar[s])
                Date.append(start_scalar[s])
                date.append(start_scalar[s])
                Dep.append(dep[s])
                Min_t.append(min_t[s])
                Max_t.append(max_t[s])
                Mean_t.append(mean_t[s])
                Stdev_t.append(stdev_t[s])
    num_date.append(len(date))
##############
#get the number of every sites
numm=num_date
print num_date
for d in range(1):
         nu=0
         for o in range(0,int(num_row_near[d])):
             nu+=numm[o]
Index_first.append(nu)
i=0
for d in range(1,len(indexs)):#len(indexs)
         i+=int(num_row_near[d-1])
         nu=0
         for o in range(i,i+int(num_row_near[d])):
             nu+=numm[o]
         Index_first.append(nu)
index_first=list(df_sites.icol(0))
index_f=list_of_groups(index_first,1) #divide a large list into small lists
rows=len(Index_first)
index_ff=[]
for s in range(0,rows):
    for i in index_f[s]:
         for j in range(int(Index_first[s])):
              index_ff.append(i)
##############
ind=list_of_groups(index_site,1) #divide a large list into small lists
rows=len(num_date)
index_s=[]
for s in range(0,rows):
    for i in ind[s]:
         for j in range(int(num_date[s])):
              index_s.append(i) 
event=list_of_groups(Event_spec,1) #divide a large list into small lists
rows=len(num_date)
Event=[]
for s in range(0,rows):
    for i in event[s]:
         for j in range(int(num_date[s])):
             Event.append(i)
data={'index_sites':np.array(index_s),'Event_spec':np.array(Event),'Latitude':np.array(Lat),
      'Longitude':np.array(Lon),'Date':np.array(Date),'Depth':np.array(Dep),
      'Min_temp':np.array(Min_t),'Max_temp':np.array(Max_t),'Mean_temp':np.array(Mean_t),
      'Stdev_temp':np.array(Stdev_t)}
frame=DataFrame(data,columns=['index_sites','Event_spec','Latitude','Longitude','Date',
                              'Depth','Min_temp','Max_temp','Mean_temp',
                              'Stdev_temp'],index=index_ff)
                              
frame.to_csv(input_dir+"merge_p_cluster.csv")             
