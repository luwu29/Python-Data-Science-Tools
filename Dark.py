#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DarkSky_API=5717e1f4efdba9d20316d0c1bb372dfe


# In[1]:


import sys
sys.path


# In[24]:


import sys

sys.path.insert( 1, 'C:\\Users\\Lu\\.ipython' )

from forecastiopy import *

import pandas as pd


# In[4]:


api_key="5717e1f4efdba9d20316d0c1bb372dfe"


# In[142]:


# Buenos={ 'lat': -34.6037,'lon': -58.3816 }
# weather = ForecastIO.ForecastIO( api_key, latitude=Buenos[ 'lat' ], longitude=Buenos[ 'lon' ] )

# current = FIOCurrently.FIOCurrently( weather )
# now = current.get()
# print( 'Now: ' + str( now[ 'temperature' ] ) )

# daily = FIODaily.FIODaily( weather )
# for day in range( 2, 7 ):
#     print( 'Day', day - 1, end = ': (' )

#     val = daily.get( day )
#     print( str( val[ 'temperatureMin' ] ), end = ',' )
#     print( str( val[ 'temperatureMax' ] ) + ')' )


# In[120]:




loc={"Anchorage, Alaska":{'lat': 61.2181, 'lon': -149.9003}, 
     "Buenos Aires, Argentia":{ 'lat': -34.6037,'lon': -58.3816 },
    "São José dos Campos, Brazil":{'lat': -23.2237, 'lon': -45.9009},
    "San José, Costa Rica":{'lat': 9.9281, 'lon': -84.0907},
    "Nanaimo, Canada":{'lat': 49.1659, 'lon': -123.9401},
    "Ningbo, China":{'lat': 29.8683, 'lon': 121.5440},
    "Giza, Egypt":{'lat': 30.0131, 'lon': 31.2089},
    "Mannheim, Germany":{'lat': 49.4875, 'lon': 8.4660},
    "Hyderabad, India":{'lat': 17.3850, 'lon': 78.4867},
    "Tehran, Iran":{'lat':35.6892, 'lon': 51.3890},
    "Bishkek, Kyrgyzstan":{'lat':42.8746, 'lon': 74.5698},
    "Riga, Latvia":{'lat': 56.9496, 'lon':24.1052},
    "Quetta, Pakistan":{'lat': 30.1798, 'lon': 66.9750},
    "Warsaw, Poland":{'lat': 52.2297, 'lon': 21.0122},
    "Dhahran, Saudia Arabia":{'lat': 26.2361, 'lon': 50.0393},
    "Madrid, Spain":{'lat': 40.4168, 'lon': -3.7038},
    "Oldham, United Kingdom":{'lat': 53.5409, 'lon': -2.1114}}


# In[122]:


data=[]
for i in loc:
    weather = ForecastIO.ForecastIO( api_key, latitude=loc[i][ 'lat' ], longitude=loc[i][ 'lon' ] )
    daily = FIODaily.FIODaily( weather )
    for day in range( 2, 7 ):
#         print(i,'Day', day - 1, end = ': (' )
        val = daily.get( day )
#         print( str( val[ 'temperatureMin' ] ), end = ',' )
#         print( str( val[ 'temperatureMax' ] ) + ')' )
        data.append({'City':i, 'Day':day-1, 'min':val[ 'temperatureMin' ], 
            'max': val[ 'temperatureMax'] })


# In[106]:


#Convert data to pd.dataframe
forcast=pd.DataFrame(data)


# In[144]:


forcast


# In[114]:


#pivoting from narrow to wide table
forcast_pivot=forcast.pivot(index='City', columns='Day', values=['max','min'])


# In[115]:


#re-index the columns
forcast_pivot.columns = [f'{i} {j}' for i, j in forcast_pivot.columns]


# In[116]:


#Compute min and max columns
forcast_pivot['max avg']=forcast_pivot[['max 1', 'max 2','max 3','max 4','max 5']].mean(axis=1)
forcast_pivot['min avg']=forcast_pivot[['min 1', 'min 2','min 3','min 4','min 5']].mean(axis=1)


# In[148]:


#Round to two decimals
forcast_csv=forcast_pivot.round(2)

#Rearrange columns
forcast_csv = forcast_csv[[ "min 1", "max 1",  "min 2", "max 2", "min 3", "max 3",
                           "min 4","max 4", "min 5", "max 5" ,'min avg','max avg']]


# In[149]:


forcast_csv


# In[150]:


#Export to csv
forcast_csv.to_csv(r'C:\Users\Lu\Documents\forcast.csv')


# In[145]:


forcast_pivot


# In[ ]:




