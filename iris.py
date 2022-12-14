#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv("iris.csv")


# In[25]:


data


# In[14]:


df=data[['Id','Species']]
df


# In[18]:


iris_setosa=data.loc[data['Species']=='Iris-setosa']
iris_setosa


# In[19]:


iris_setosa.mean()


# In[21]:


iris_setosa.std()


# In[23]:


iris_setosa.median()


# In[27]:


data.info()


# In[28]:


import matplotlib.pyplot as plt


# In[30]:


plt.hist(data['SepalLengthCm'])
plt.show()


# In[31]:


plt.hist(data['SepalWidthCm'])
plt.show()


# In[33]:


plt.boxplot(data['SepalWidthCm'])
plt.show()


# In[35]:


df=[data['SepalWidthCm'],data['SepalLengthCm']]
plt.boxplot(df)
plt.show()


# In[36]:


import seaborn as sns


# In[45]:


ir=data.corr()
heatmap=sns.heatmap(data)
plt.show()


# In[ ]:




