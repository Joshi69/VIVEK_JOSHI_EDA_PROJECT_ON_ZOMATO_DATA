#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("zomato.csv", encoding="latin-1")


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[8]:


df.shape


# In[70]:


sns.heatmap(df.isnull(),cbar=False,cmap="coolwarm")
plt.show()


# In[10]:


df_country=pd.read_excel("country-code.xlsx")


# In[11]:


df_country.head()


# In[12]:


df.columns


# In[66]:


final_df = pd.merge(df,df_country,on="Country Code",how="left")
final_df


# In[14]:


final_df.head(2)


# In[15]:


final_df.dtypes


# In[16]:


final_df.columns


# In[67]:


country_names=final_df.Country.value_counts().index
country_names


# In[68]:


country_value=final_df.Country.value_counts().values
country_value


# In[39]:


plt.pie(country_value[:3],labels=country_names[:3],autopct="%1.2f%%")
plt.show


# observation:zomato maximum transaction and records are from  india after that usa and then united kingdom 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[20]:


final_df.columns


# In[21]:


ratings=final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'rating count'})


# In[22]:


ratings


# 1. when rating is between 4.5 to 4.9-->excellent
# 2. when rating is between 4.0 to3.4-->very good
# 3. when rating is between 3.5to3.9 -->good
# 4. when rating is between 3.0to3.4 -->average
# 5. when rating is between 2.5to2.9 -->average 
# 6. when rating is between 2.0to2.4 -->poor
# 

# In[23]:


fig=plt.figure(figsize=(12,6))
sns.barplot(x="Aggregate rating",y="rating count",data=ratings)
plt.show()



# In[24]:


fig=plt.figure(figsize=(12,6))
sns.barplot(x="Aggregate rating",y="rating count",data=ratings,hue="Rating color",palette="Accent")
plt.show()


# observation :
#            1. not rated count is very high
#            2. maximum  no of rating between 2.5 to 3.4

# In[32]:


sns.countplot(x="Rating color",data=ratings,palette="Accent")
plt.show()


# In[26]:


final_df.columns


# In[30]:


# find the country that giving 0 rating
final_df.groupby(['Aggregate rating','Country']).size().reset_index()


# observations:
# maximum numbers of rating are from indian customers

# In[31]:


# find out the which currency is used by which country?
final_df.columns


# In[33]:


final_df.groupby(['Country','Currency']).size().reset_index()


# In[34]:


# which country have onlinr delieveries option?
final_df.columns


# In[35]:


final_df.groupby(['Country','Has Online delivery']).size().reset_index()


# observation:
# 1.online delieveries are available in india and uae

# In[36]:


# create a pie chary for cities distribution
final_df.columns


# In[60]:


city_labels=final_df.City.value_counts().index
city_labels


# In[45]:


city_values=final_df.City.value_counts().values
city_values


# In[65]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct="%1.2f%%")
plt.show


# observation:
# 68.87 % distributed in delhi ,14.07 % distributed in gurgaon,13.59 % distributed in noida,3.16 % in faridabadand 0.31 % in ghaziabad
