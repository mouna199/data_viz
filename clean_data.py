#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

df=pd.read_csv("earthquake.csv")
#takes the three time variable

df['year'] = pd.DatetimeIndex(df['time']).year
df['month'] = pd.DatetimeIndex(df['time']).month
df['day'] = pd.DatetimeIndex(df['time']).day
# creates a dataframe with the six variables we are intreseted in, and sort them by time ascending. 
my_data=df[["year","month","day", "mag","latitude","longitude"]].sort(["year","month","day"],ascending=[1, 1,1])
# creates a file names example, that we will use for the visualization .

my_data.to_csv('example.csv')
