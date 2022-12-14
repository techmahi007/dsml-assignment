#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("covid_vaccine_statewise.csv")


# In[3]:


data


# In[6]:


data.describe()


# In[7]:


data.info()


# In[41]:


males_vaccinated=data["Male(Individuals Vaccinated)"]


# In[42]:


males_vaccinated


# In[54]:


males_vaccinated.dropna()


# In[44]:


males_vaccinated.sum()


# In[46]:


females_vaccinated=data["Female(Individuals Vaccinated)"]


# In[82]:


females_vaccinated


# In[81]:


females_vaccinated.dropna(inplace=True)
females_vaccinated


# In[49]:


females_vaccinated.sum()


# In[74]:


data.nunique()


# In[75]:


data.isna().sum()


# In[70]:


Sessions=data['Sessions'].dropna()


# 

# In[72]:


Sessions.astype(int)


# In[73]:


data['Sessions']


# In[84]:


x=data.mean()
data.fillna(x,inplace=True)


# In[85]:


data


# In[86]:


data1=data.groupby("State")
data1["First Dose Administered"].count()


# In[87]:


data1["Second Dose Administered"].count()


# In[ ]:




