#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')


# In[6]:


df1 = pd.read_csv('Documents/groundhog predictions dataset/groundhogs.csv')


# In[7]:


df2= pd.read_csv('Documents/groundhog predictions dataset/predictions.csv')


# In[15]:


df1 = df1.merge(df2,on='id',how='inner')


# In[9]:


df1.shape


# In[17]:


df1.head()


# In[18]:


df1.dtypes


# In[19]:


df1.columns


# In[32]:


df1 = df1[['id', 'slug', 
     #'shortname', 
     'name', 'city', 'region', 'country',
       'latitude', 'longitude', 
     #'source', 
     #'current_prediction', 
     'is_groundhog',
       'type', 'active', 'description', 
     #'image', 'predictions_count', 
     'year',
       'shadow' #'details'
          ]].copy()


# In[27]:


df1.head(3)


# In[29]:


df1.dtypes


# In[33]:


df1.isna().sum()


# In[37]:


df1.loc[df1.duplicated(subset=['year'])]


# In[41]:


df1.query('year == 2022')


# In[42]:


df1.duplicated(subset=['name','city','year']).sum()


# In[45]:


df1['year'].value_counts()


# In[59]:


pl1 = df1[['city','country']].value_counts() \
    .head(10) \
    .plot(kind='bar', title = 'Top 10 Cities with the most groundhog predictions')

pl1.set_xlabel('City and Country')
pl1.set_ylabel('Historical number of predictions')


# In[75]:


pl2 = df1[['name','type']].value_counts() \
    .head(10) \
    .plot(kind='bar', title = 'Top 10 Most active groundhogs and their type')

pl2.set_ylabel('Number of predictions')
pl2.set_xlabel('Name and type')
