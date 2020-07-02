#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Ex02_data.csv', sep=";", header= 0, parse_dates=[0], index_col=0)

#Min Values
tmax = data.loc[:, 'Tmax'].min()
tmin = data.loc[:, 'Tmin'].min()
rrmin = data.loc[:, 'RR'].min()

#Max values
Tmax = data.loc[:, 'Tmax'].max()
Tmin = data.loc[:, 'Tmin'].max()
rrmax = data.loc[:, 'RR'].max()

data_mean = data.resample('M').mean()

#anomalies calculation
tmaxanom = data.Tmax - data.Tmax.mean()
tminanom = data.Tmin - data.Tmin.mean()
monthlytmax = tmaxanom.resample('1m').mean()
monthlytmin= tminanom.resample("1m").mean()


# In[ ]:





# In[ ]:


#1
fix,ax=plt.subplots(3,1,figsize=(16,10))
plt.style.use("seaborn")
ax[0].plot(data_mean.index,data_mean["Tmax"],label="MAX Temperature",color="r",linestyle="-")
ax[0].set_ylabel("Degree Celsius")
ax[0].set_title("Max Temperature")
ax[1].plot(data_mean.index,data_mean["Tmin"],label="Min Temperature",color="g",linestyle="-")
ax[1].set_title("Min Temperature")
ax[1].set_ylabel("Degree Celsius")
ax[2].plot(data_mean.index,data_mean["RR"],label="RR",linestyle="-")
ax[2].set_title("RR")
ax[2].set_ylabel("Degree Celsius")
plt.show()




# In[ ]:





# In[ ]:


df=data.resample('m')


# In[ ]:


#2
fix,ax=plt.subplots(2,1,figsize=(16,10))
ax[0].plot(monthlytmax,color="r",lw=2)
ax[0].set_ylabel("Max Temperature anomaly")
ax[1].plot(monthlytmin,color="g",lw=2)
ax[1].set_ylabel("Min Temperature anomaly")


# In[ ]:


x=monthlytmax[monthlytmax.index.month==6]
y=monthlytmax[monthlytmax.index.month==7]
z=monthlytmax[monthlytmax.index.month==8]
df=x.append([y,z])

x1=monthlytmax[monthlytmin.index.month==6]
y1=monthlytmax[monthlytmin.index.month==7]
z1=monthlytmax[monthlytmin.index.month==8]
df1=x.append([y1,z1])

fix,ax=plt.subplots(2,1,figsize=(16,10))
ax[0].plot(x,color="r",lw=2,label="June")
ax[0].plot(y,color="g",lw=2,label="July")
ax[0].plot(z,color="b",lw=2,label="August")
ax[0].legend()
ax[1].plot(x1,color="r",lw=2,label="June")
ax[1].plot(y1,color="g",lw=2,label="July")
ax[1].plot(z1,color="b",lw=2,label="August")
ax[1].legend()

