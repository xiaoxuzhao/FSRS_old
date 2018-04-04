# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:17:00 2018
plot temperature and depth 
@author: xiaoxu zhao
"""
from pandas import read_csv
from dateutil import parser
import matplotlib.pyplot as plt
#####################
#HARDCODES
input_dir='C:/Users/11307/Documents/python/getfsrs/all files/'
save_dir='C:/Users/11307/Documents/python/getfsrs/pictures/'
#input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
#save_dir='/home/zdong/xiaoxu/FSRS/figure/'
s=8
index_mt3=[1,16,73,97,145,216,250,329,369,418]
#####################
df=read_csv(input_dir+'merge_date_good_depth.csv')
dfh=read_csv(input_dir+'fsrs_sites(1000days).csv')
#index_1000=list(dfh.icol(0))    #lunix
#index_first=list(df.icol(0))    #lunix
index_1000=list(dfh.iloc[:,0])
index_first=list(df.iloc[:,0])
row_index=[]
for i in range(len(index_first)):
    if index_first[i]==index_1000[s]:
            row_index.append(i)
            p=index_1000[s]
df[row_index[0]:row_index[-1]].to_csv(input_dir+str(p)+"_site_sort_depth.csv", index=False)
df=read_csv(input_dir+str(p)+"_site_sort_depth.csv")
#df = df.sort("Date")  #lunix
df = df.sort_values("Date")
index_sites=df["index_sites"]
date=df["Date"]
Mean_temp=df["Mean_temp"]
depth=df["Depth"]
####################### 
#get unique station value in order
index_sites=df["index_sites"]
index_sites=list(index_sites)
index = list(set(index_sites))
index.sort(key=index_sites.index)
#######################
#Get the first occurrence of the index value
first_appear=[]
for i in range(len(index)):
    q=index_sites.index(index[i])
    first_appear.append(q)
####################### 
#Convert date columns to time format,and only need top ten
Date=[]
for i in date:
          Date.append(parser.parse(i[0:10]))
fig, ax =plt.subplots()
# Plot y1 vs x in blue on the left vertical axis.
plt.xlabel("Date ")
plt.ylabel("Temperature [C]", color="b")
plt.tick_params(axis="y", labelcolor="b")
#color=["pink","orange","brown","green","black","red","blue","yellow","purple","cyan","magenta","chocolate","beige","lime"]

for s in range(len(index)):
      a,dep=0,0
      for i in range(len(date)):
           if index_sites[i]==index[s]:
                a+=1
                dep+=depth[i]
      plt.plot(Date[first_appear[s]:first_appear[s]+a], Mean_temp[first_appear[s]:first_appear[s]+a],color="b",linewidth=1.5, linestyle="-")

#plt.plot(Date,Mean_temp, "b-", linewidth=1)
plt.title("the site 369 Temperature and Depth")
fig.autofmt_xdate(rotation=50)
plt.twinx()
plt.ylabel("Depth", color="r")
plt.tick_params(axis="y", labelcolor="r")
for s in range(len(index)):
      a,dep=0,0
      for i in range(len(date)):
           if index_sites[i]==index[s]:
                a+=1
      plt.plot(Date[first_appear[s]:first_appear[s]+a], depth[first_appear[s]:first_appear[s]+a],color="r",linewidth=1.5, linestyle="-")
#plt.plot(Date, depth, "r-", linewidth=1)
plt.savefig(save_dir+"369_site_temperature_depth.png")  
plt.show()
