#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


data=pd.read_csv("House_Rent_Dataset.csv")
data.columns


# In[16]:


data1=data.groupby("Rent")
data1.describe()


# In[19]:


data2=data.groupby("Area")
data2.describe()


# In[ ]:




