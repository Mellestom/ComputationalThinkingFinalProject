#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 11:32:33 2022

@author: thomas
"""

import pandas as pd
from numpy import nan
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv('Traffic_Crashes_2021.csv')

'''
def Injury(file):
    
    
    # Create list of Injury numbers
    Injuries_Total = file['INJURIES_TOTAL'].tolist()
    # Create list of Fatality numbers
    Injuries_Fatal = file['INJURIES_FATAL'].tolist()
    
    # Remove NA values
    Injuries_Total = [item for item in Injuries_Total if not (pd.isnull(item))==True]
    Injuries_Fatal = [item for item in Injuries_Fatal if not (pd.isnull(item))==True]
    No_Injury = Injuries_Total.count(0)
    
    # Get total numbers for Crashes, Injuries, and Fatalities
    TOTAL_CRASHES = (Injuries_Total)
    INJURIES_TOTAL = sum(Injuries_Total)
    INJURIES_FATAL = sum(Injuries_Fatal)
    data = [No_Injury,INJURIES_TOTAL,INJURIES_FATAL]
    
    # Create Lables for Pie Chart
    labels = ['No Injury','Only Injuries','Fatalities']
    colors = ('lightblue','orange','green')
    explode = (0,0.1,0.2)
    fig = plt.figure(figsize = (10,7))
    plt.pie(data,labels = labels,
        colors = colors,
        explode = explode,
        startangle=90,
        autopct='%.1f%%',
        pctdistance=1, 
        labeldistance=1.2,
        textprops={'color':'red','fontsize':'15'})
    
    plt.savefig('injury.png')
    
    print(No_Injury)
    print(INJURIES_TOTAL)
    print(INJURIES_FATAL)

Injury(data)
'''
'''
def NotifiedDelay(file):
    
    df = file
    
    
    
    notify_df = df.loc[:, ['CRASH_DATE', 'DATE_POLICE_NOTIFIED']]

    
    notify_df['CRASH_DATE'] = notify_df['CRASH_DATE'].astype('datetime64[m]')
    notify_df['DATE_POLICE_NOTIFIED'] = notify_df['DATE_POLICE_NOTIFIED'].astype('datetime64[m]')
    
    notify_df['TIME_DIF'] = ((pd.to_datetime(notify_df['CRASH_DATE']) - 
                            pd.to_datetime(notify_df['DATE_POLICE_NOTIFIED']))
                                .astype('<m8[m]').astype(int))
    

    notify_df = notify_df[notify_df['TIME_DIF'].between(0, 60)]
  
    print(notify_df)
    
    
NotifiedDelay(data)
'''
'''

def C1(file):
    
    df = file
    
    # Create list of crash dates
    df[['month','day','year']] = df.CRASH_DATE.str.split('/', expand=True)
        
    
    freq = pd.Series(df['month'])
    
    freq = freq.value_counts()
    labels = ('June','Oct','July','Aug','Sep','May','Nov','Dec','Feb','Apr','Mar','Jan')
    
    plt.bar(labels,freq)
    plt.show()
    
    print('Our analysis shows that in general crashes occur at a higher rate in the summer than the winter with October being a large outlier as well as April')
    
C1(data)
'''

def C2(file):
    
    df = file
    
    speed = df.groupby(['POSTED_SPEED_LIMIT','DAMAGE']).size()
    print(speed)

C2(data)


