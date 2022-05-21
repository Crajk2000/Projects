#!/usr/bin/env python
# coding: utf-8

# # <font color = 'darkred'> ...Rajkumar Choudhary... </font>
# ## <font color = 'darkblue'> ...Roll No.:- DS5B-2024... </font>
# 
# # "Project on Analysis of Unemployment in India in Last Five Years from 14th May 2022 to 13th May 2022". 

# ## "This dataset contains the unemployment rate of all the states in India".
# 
# * States = states in India
# * Date = date which the unemployment rate observed
# * Frequency = measuring frequency (Monthly)
# * Estimated Unemployment Rate (%) = percentage of people unemployed in each States of India
# * Estimated Employed = Number of people employed
# * Estimated Labour Participation Rate (%) = The labour force participation rate is the portion of the working population in the 16-64 years' age group in the economy currently in employment or seeking employment.

# # "Index".
# 
# * <a href="#'Import-data-and-Neccessary-Libraries-for-further-use'.">"Import data and Neccessary Libraries for further use".</a>
# * <a href="#'Perform-Statistics-process-on-data'.">"Perform Statistics process on data".</a>
# * <a href="#'groupby-data-by-region-wise'.">"groupby data by region wise".</a>
# * <a href="#'Exploratory-Data-Analysis'.">"Exploratory Data Analysis".</a>
# * <a href="#'plot-boxplot-of-Unemployment-Rate-by-Statewise'.">"plot boxplot of Unemployment Rate by Statewise".</a>
# * <a href="#'Draw-Scatterplot-on-the-data'.">"Draw Scatterplot on the data".</a>
# * <a href="#'Draw-bar-chart-for-Average-Unemployment-Rate-in-each-State'.">"Draw bar chart for Average Unemployment Rate in each State".</a>
# * <a href="#'Visualization-on-the-Data'.">"Visualization on the Data".</a>
# * <a href="#'Show-heatmap-between-entities'.">"Show heatmap between entities".</a>
# * <a href="#'Hisplot-figure-on-Estimated-Employed-data-by-region'.">"Hisplot figure on Estimated Employed data by region".</a>
# * <a href="#'Hisplot-Figure-on-Estimated-Unemployment-Rate-by-Region'.">"Hisplot Figure on Estimated Unemployment Rate by Region".</a>
# * <a href="#'Top-States-by-Estimated-Unemployment-Rate-in-India'.">"Top States by Estimated Unemployment Rate in India".</a>
# * <a href="#'Plotting-Sunburst-Figure-on-whole-data-to-show-Specifically-Unemployment-Rate-in-India-in-last-five-years'.">"Plotting Sunburst Figure on whole data to show Specifically Unemployment Rate in India in last five years".</a>
# * <a href="#'Unemployment-during-covid19-Pandemic'.">"Unemployment during covid19 Pandemic".</a>
# * <a href="#'Most-impacted-states-&-Union-Territory'.">"Most impacted states & Union Territory".</a>
# * <a href="#'Impact-of-lockdown-on-employment-across-states'.">"Impact of lockdown on employment across states".</a>
# * <a href="#'Scatter-plot-on-latitude-and-longitude'.">"Scatter plot on latitude and longitude".</a>
# * <a href="#'Map-of-india-showing-states-using-latitude-and-longitude'."> "Map of india showing states using latitude and longitude".</a>
# * <a href="#'Get-the-whole-running-time-duration-of-this-project'.">"Get the whole running time duration of this project.</a>
# * <a href="#End...">"End".</a>

# # 'Import data and Neccessary Libraries for further use'.
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import calendar
from datetime import datetime as dt
start_time=dt.now()

import plotly.io as pio
import warnings
warnings.filterwarnings('ignore')


# In[2]:


pio.templates


# ## "Getting the data from the source".

# In[3]:


data = pd.read_csv("D:/CSV Files/Unemployment.csv")
data.head()


# ## "Adding Column In Data". 

# In[4]:


data["Location"]= data['States']+", "+data["Country"]


# ## "Show data and see how many rows and columns are there".

# In[5]:


data


# ## "Checking is there any null values in the columns or not".

# In[6]:


print(data.isnull().sum())


# ## "Renaming the columns for simplycity".

# In[7]:


data.columns= ["States","Country","Date","Frequency",
               "Estimated_Unemployment_Rate",
               "Estimated_Employed",
               "Estimated_Labour_Participation_Rate",
               "Region","Latitude","Longitude","Location"]
data


# In[8]:


data['Date'] = pd.to_datetime(data['Date'],dayfirst=True)


# In[9]:


data['Frequency']= data['Frequency'].astype('category')


# ## "Adding Month Column in the data".

# In[10]:


data['Month'] =  data['Date'].dt.month


# In[11]:


data['Month_int'] = data['Month'].apply(lambda x : int(x))


# In[12]:


data['Month_name'] =  data['Month_int'].apply(lambda x: calendar.month_abbr[x])


# In[13]:


data['Region'] = data['Region'].astype('category')


# In[14]:


data.drop(columns='Month',inplace=True)
data.head(3)


# ## 'Perform Statistics process on data'.

# ### And get the mean, min, max and standard deviation of Estimated Unemployment Rate, Estimated Employed, Estimated Labour Participation Rate. 

# In[15]:


data_stats = data[['Estimated_Unemployment_Rate',
      'Estimated_Employed', 'Estimated_Labour_Participation_Rate']]


round(data_stats.describe().T,2)


# ## 'groupby data by region wise'.

# In[16]:


region_stats = data.groupby(['Region'])[['Estimated_Unemployment_Rate','Estimated_Employed','Estimated_Labour_Participation_Rate']].mean().reset_index()

region_stats = round(region_stats,2)


region_stats


# ## "Cheking data size, how many rows and columns are there and unique values".

# In[17]:


data.size


# In[18]:


data.shape


# In[19]:


data.nunique


# ## "checking not null values, data types of the data and axes in the data".

# In[20]:


data.notnull


# In[21]:


data.dtypes


# In[22]:


data.axes


# ## 'Exploratory Data Analysis'.

# ## 'plot boxplot of Unemployment Rate by Statewise'.

# In[23]:


fig = px.box(data,x='States',y='Estimated_Unemployment_Rate',color='States',title='Unemployment_rate',template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()


# ## 'Draw Scatterplot on the data'.

# In[24]:


fig = px.scatter_matrix(data,template='plotly',
    dimensions=['Estimated_Unemployment_Rate','Estimated_Employed',
                'Estimated_Labour_Participation_Rate'],
    color='Region')
fig.show()


# ## 'Draw bar chart for Average Unemployment Rate in each State'.

# In[25]:


plot_ump = data[['Estimated_Unemployment_Rate','States']]

df_unemp = plot_ump.groupby('States').mean().reset_index()

df_unemp = df_unemp.sort_values('Estimated_Unemployment_Rate')

fig = px.bar(df_unemp, x='States',y='Estimated_Unemployment_Rate',color='States',
            title='Average Unemployment Rate in each state',template='plotly')

fig.show()


# # 'Visualization on the Data'.

# In[26]:


#Heatmap.
heat_maps = data[['Estimated_Unemployment_Rate',
       'Estimated_Employed', 'Estimated_Labour_Participation_Rate']]

heat_maps = heat_maps.corr()

plt.figure(figsize=(10,6))
sns.set_context('notebook',font_scale=1)
sns.heatmap(heat_maps, annot=True,cmap='winter');


# ## 'Show heatmap between entities'.

# In[27]:


#Heatmap on two entities.
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr())
plt.show()


# ## 'Hisplot figure on Estimated Employed data by region'.

# In[28]:


data.columns= ["States","Country","Date","Frequency",
               "Estimated_Unemployment_Rate",
               "Estimated_Employed",
               "Estimated_Labour_Participation_Rate",
               "Region","Location","Longitude","Latitude","Month_int","Month_name"]
plt.figure(figsize=(15,8))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated_Employed", hue="Region", data=data)
plt.show()


# ## 'Hisplot Figure on Estimated Unemployment Rate by Region'.

# In[29]:


plt.figure(figsize=(18, 10))
plt.title("Unemployment in India")
sns.histplot(x="Estimated_Unemployment_Rate", hue="Region", data=data)
plt.show()


# ## 'Top States by Estimated Unemployment Rate in India'.

# In[30]:


plt.rcParams['figure.figsize'] = (15, 5)
color = plt.cm.copper(np.linspace(0, 2, 50))
data['States'].value_counts().head(40).plot.bar(color = color)
plt.title('Top States by Estimated Unemployment Rate',color ='darkblue', fontsize = 20)
plt.xlabel('States', color = 'darkred', size = 15,)
plt.ylabel('Estimated_Unemployment_Rate', color = 'darkred', size = 15)
plt.xticks(rotation = 50)
plt.grid()
plt.show()


# ## 'Plotting Sunburst Figure on whole data to show Specifically Unemployment Rate in India in last five years'.

# In[31]:


unemploment = data[["States", "Region", "Estimated_Unemployment_Rate"]]
figure = px.sunburst(unemploment, path=["Region", "States"], 
                     values="Estimated_Unemployment_Rate", 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")
figure.show()


# # 'Unemployment during covid19 Pandemic'.
# ## "CalculatingUnemployment Rate before and after Lockdown"'.

# In[32]:


lock = data[(data['Month_int'] >= 4) & (data['Month_int'] <=7)]

bf_lock = data[(data['Month_int'] >= 1) & (data['Month_int'] <=4)]


# In[33]:


g_lock = lock.groupby('States')['Estimated_Unemployment_Rate'].mean().reset_index()

g_bf_lock = bf_lock.groupby('States')['Estimated_Unemployment_Rate'].mean().reset_index()


g_lock['Unemployment Rate before lockdown'] = g_bf_lock['Estimated_Unemployment_Rate']

g_lock.columns = ['States','Unemployment Rate after lockdown','Unemployment Rate before lockdown']

# Show only five states according to alphabetics A to Z.
g_lock.head(5)


# In[34]:


# percentage change in unemployment rate.
g_lock['percentage change in unemployment'] = round(g_lock['Unemployment Rate after lockdown'] - g_lock['Unemployment Rate before lockdown']/g_lock['Unemployment Rate before lockdown'],2)


# In[35]:


plot_per = g_lock.sort_values('percentage change in unemployment')


# In[36]:


# percentage change in unemployment after lockdown.

fig = px.bar(plot_per, x='States',y='percentage change in unemployment',color='percentage change in unemployment',
            title='percentage change in Unemployment in each state after lockdown',template='ggplot2')

fig.show()


# ## 'Most impacted states & Union Territory'.
# 
# * Haryana
# * Jharkhand
# * Rajasthan
# * Puducherry
# * Himachal Pradesh

# ## 'Impact of lockdown on employment across states'.

# In[37]:


# function to sort value based on impact.

def sort_impact(x):
    if x <= 10:
        return 'impacted States'
    elif x <= 20:
        return 'hard impacted States'
    elif x <= 30:
        return 'harder impacted States'
    elif x <= 40:
        return 'hardest impacted States'
    return x    


# In[38]:


plot_per['impact status'] = plot_per['percentage change in unemployment'].apply(lambda x:sort_impact(x))


# In[39]:


fig = px.bar(plot_per, y='States',x='percentage change in unemployment',color='impact status',
            title='Impact of lockdown on employment across states',template='ggplot2',height=650)


fig.show()


# ## 'Scatter plot on latitude and longitude'.

# In[40]:


import matplotlib.pyplot as plt

#get data 
df = pd.read_csv("D:/CSV Files/Unemployment.csv")
plt.scatter(x=df['Latitude'], y=df['Longitude'])
plt.xlabel('Latitude', color = 'darkred', size = 15,)
plt.ylabel('Longitude', color = 'darkred', size = 15)
plt.xticks(rotation = 0)
plt.show()


# ## 'Map of india showing states using latitude and longitude'.

# In[41]:


# import packages
import pandas as pd
import plotly.express as px
import numpy as np

#get data 
data1 = pd.read_csv("D:/CSV Files/Unemployment.csv")
data1.head()

# two-line code
fig = px.scatter_mapbox(data1, lat=data1['Latitude'], lon=data1['Longitude'], color='States', zoom=3, mapbox_style='open-street-map')
fig.show()


# ## 'Get the whole running time duration of this project'.

# In[42]:


end_time=dt.now()
print('Duration: {}'.format(end_time-start_time))


# # <font color = darkred>..."Thank you"...</font>
# ## Project by Rajkumar Choudhary...
# ### School of Data Science and Forecasting...

# # End...
