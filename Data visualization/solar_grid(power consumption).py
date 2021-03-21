#!/usr/bin/env python
# coding: utf-8

# In[33]:


"""importing csv file and loading the data"""
import pandas as pd
import numpy as np
x1= pd.read_csv('solar_power.csv')
print(x1)


# In[6]:


"""plot of solar,ac and battery columns"""
import matplotlib.pyplot as plt
plt.figure(figsize=(20,20))
x1.plot(x='created_at', y=['SOLAR', 'AC','BATTERY'])
plt.show()


# In[28]:


"""maximum value of solar is printed and the histogram is plotted between the days of month and solar energy used"""
maximum_solar= x1["SOLAR"]
max_value_1 = maximum_solar.max()
print(max_value_1)
plt.figure(figsize=(20,20))
x1.plot.hist(x='created_at', y='SOLAR')
plt.show()


# In[29]:


"""maximum value of AC is printed and the histogram is plotted between the days of month and AC"""
maximum_ac= x1["AC"]
max_value_2 = maximum_ac.max()
print(max_value_2)
plt.figure(figsize=(20,20))
x1.plot.hist(x='created_at', y='AC')
plt.show()


# In[30]:


"""maximum value of battery is printed and the histogram is plotted between the days of month and battery energy """
maximum_battery= x1["BATTERY"]
max_value_3 = maximum_battery.max()
print(max_value_3)
plt.figure(figsize=(20,20))
x1.plot.hist(x='created_at', y='BATTERY')
plt.show()


# In[31]:


"""maximum value of credits is printed and the histogram is plotted between the days of month and credits gained"""
maximum_credits= x1["CREDITS"]
max_value_4 = maximum_credits.max()
print(max_value_4)
plt.figure(figsize=(20,20))
x1.plot.hist(x='created_at', y='CREDITS')
plt.show()


# In[20]:


"""scatter  plot is plotted between solar energy and AC"""
plt.scatter(maximum_solar,maximum_ac)
plt.show()


# In[24]:


"""scatter plot is plotted between battery energy stored and credits gained"""
plt.scatter(maximum_battery,maximum_credits)
plt.show()


# In[26]:


"""Box plot of all the columns i.e..solar energy,AC,Battery,Credits is plotted"""
x1.plot.box(grid='True')


# In[ ]:




