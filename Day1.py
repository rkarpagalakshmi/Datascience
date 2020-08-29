#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


import seaborn as sns
fifa_csv = pd.read_csv("C:/Users/Lakshmisaravanan/Desktop/Datascience/data-for-datavis/fifa.csv",index_col = "Date",parse_dates=True)


# In[21]:


fifa_csv.head()


# In[23]:


sns.lineplot(data = fifa_csv)


# In[24]:


plt.figure(figsize=(17,6))
plt.title("Scores of the countries")
plt.xlabel("Date in Years")

sns.set_style('dark')
sns.lineplot(data = fifa_csv['ARG'],label = 'Argentina')
sns.lineplot(data = fifa_csv['GER'],label = 'Germany')


# In[25]:



plt.figure(figsize=(17,6))
plt.title("Scores of the countries")
plt.xlabel("Date in Years")

sns.set_style(style ='whitegrid')
sns.lineplot(data = fifa_csv['ARG'],label = 'Argentina')
sns.lineplot(data = fifa_csv['GER'],label = 'Germany')


# plt.figure(figsize=(17,6))
# plt.title("Scores of the countries")
# plt.xlabel("Date in Years")
# 
# sns.set_style('darkgrid')
# sns.lineplot(data = fifa_csv['ARG'],label = 'Argentina')
# sns.lineplot(data = fifa_csv['GER'],label = 'Germany')

# In[29]:


flight_csv = pd.read_csv("C:/Users/Lakshmisaravanan/Desktop/Datascience/data-for-datavis/flight_delays.csv",index_col="Month")


# In[30]:


flight_csv.head()


# In[31]:


plt.figure(figsize=(15,7))
plt.title("Average delays in the Inceptez airlines (month)")

sns.barplot(x=flight_csv.index,y =flight_csv['AA'])

#Adding Y-labels 
plt.ylabel("Arrival Delay in minutes")


# In[32]:


plt.figure(figsize=(15,7))
#Heatmap
sns.heatmap(data = flight_csv)


# In[33]:


plt.figure(figsize=(15,7))
#Heatmap
corr = flight_csv.corr()
sns.heatmap(corr,vmin=-1,vmax=1,center = 0)


# In[34]:


plt.figure(figsize=(15,7))
#Heatmap
corr = flight_csv.corr()
sns.heatmap(corr,vmin=-1,vmax=1,center = 0,annot = True)


# In[ ]:




