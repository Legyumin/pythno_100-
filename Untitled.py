#!/usr/bin/env python
# coding: utf-8

# ### 결측열 삭제

# In[5]:


import pandas as pd


# In[6]:


path = 'data1.csv'


# In[15]:


df = pd.read_csv(path, encoding='cp949')


# In[16]:


df


# In[18]:


df.shape


# In[21]:


df_null_count = df.isnull().sum()


# In[25]:


df_null_count=df_null_count.reset_index()


# In[28]:


df_null_count


# In[30]:


df_null_count.tail(2)


# In[36]:


df_3=null_count.sort_values(by='index',ascending =True).head(2)


# In[35]:


df_drop=df_3['index']


# In[ ]:


df_drop.to_list()

