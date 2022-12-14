#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
d = {
    'Algothime': ['KNN', 'SVM', 'MLP'],
    'Param. 1': ['-', '-', '-'],
    'Param. 2': ['-', '-', '-'],
    'Plage param. 1': ['-', '-', '-'],
    'Plage param. 2': ['-', '-', '-']
 }
df = pd.DataFrame(data=d)


# In[21]:


true_positive=1
true_negative=90
false_positive=1
false_negative=8
total_positive=2


# In[22]:


Accuracy=true_positive+true_negative/100
Precision=true_positive/true_positive+false_positive
Recall=true_positive/true_positive+false_negative
Error_rate=1-Accuracy

print(Accuracy)
print(Precision)
print(Recall)
print(Error_rate)


# In[ ]:


def Accuracy():
    

