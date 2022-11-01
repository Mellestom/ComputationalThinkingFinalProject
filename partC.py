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

pd.set_option('display.max_rows', None)

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


def C2(file):
    
    df = file
    
    speed = df.groupby(['POSTED_SPEED_LIMIT','DAMAGE']).size()
    damage = df.groupby('DAMAGE').size()
    
    print(speed)
    print(damage)
    speed.plot(kind='line')
    plt.show()
    print('Our analysis shows that the 30mph speed limit zone results in the highest amount of crash damage and most crashes that occurred resulted in over $1,500 in damages')

C2(data)


def C3(file):
    
    df = file
    
    lighting = df.groupby('LIGHTING_CONDITION').size()
    
    print(lighting)
    lighting.plot(kind='bar')
    plt.show()
    print('Our Analysis shows that most accidents occur during daylight or with lighted roads and not in darkness')
    
C3(data)

def C4(file):
    
    df = file
    
    speed = df.groupby('POSTED_SPEED_LIMIT').size()

    print(speed)
    speed.plot(kind='pie')
    print('Our analysis shows that the overwhelming majority of accidents occur in 30 mph speed limit zones and occur less frequently at higher speeds')
    
C4(data)


