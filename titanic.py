#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("train.csv")
data


# In[3]:


data.describe()


# In[25]:


import seaborn as sm


# In[5]:


data.info()


# In[10]:


col=data[["PassengerId","Survived","Name"]]
col


# In[19]:


data1=pd.read_csv("train.csv",index_col="PassengerId")
ans=data1.loc(["1"])
print(ans)


# In[21]:


data1=data.iloc[[3,4,5,6]]
print(data1)


# In[22]:


data1=data.sort_values(by=['Survived'])
print(data1)


# In[24]:


import matplotlib.pyplot as plt
plt.hist(data['Fare'])
plt.show()


# In[27]:


data1=sm.heatmap(data.corr())
plt.show()


# In[ ]:




