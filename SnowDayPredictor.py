#!/usr/bin/env python
# coding: utf-8

# # Future Snow Day Calculation

# In[2]:


import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()



# # Importing dataset
# 1. Since data is in form of excel file we have to use pandas read_excel to load the data
# 2. After loading it is important to check complete information of data as it can inidicate many of hidden information such as null values in a column or a row.
# 3. Check whether nay null values are there or not. If it is present following can be done, 
#      A. Imputing data using imputation method in sklearn.
#      B. Filling NaN values with mean, median, and mode using fillna() method
# 4. Describe data ---> which can give statistical analysis

# In[21]:


train_data = pd.read_csv("CanadaSnow.csv")
train_data


# In[8]:


train_data.info()


# In[9]:


train_data["Date/Time"].value_counts()


# In[10]:


train_data.dropna(inplace = True)


# In[11]:


train_data.isnull().sum()


# In[12]:


train_data.shape


# In[13]:


train_data.head()


# In[14]:


train_data = train_data.fillna(method="ffill")


# In[16]:


train_data.apply(pd.isnull).sum()/train_data.shape[0]


# In[18]:


train_data.index


# In[24]:


train_data.apply(lambda x:(x==999).sum())


# In[26]:


sns.catplot(x="Max Temp (C)", y="Min Temp (C)", data=train_data.sort_values("Min Temp (C)", ascending = False), kind = "boxen", height=6, aspect=3)
plt.show()


# In[31]:


sns.catplot(x="Date/Time", y="Total Snow (cm)", data=train_data.sort_values("Total Snow (cm)", ascending = False), kind = "boxen", height=6, aspect=3)
plt.show()


# In[32]:


sns.catplot(x="Total Snow (cm)", y="Min Temp (C)", data=train_data.sort_values("Min Temp (C)", ascending = False), kind = "boxen", height=6, aspect=3)
plt.show()


# In[ ]:




