#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

df=pd.read_csv("earthquake.csv")


df['year'] = pd.DatetimeIndex(df['time']).year
df['month'] = pd.DatetimeIndex(df['time']).month
df['day'] = pd.DatetimeIndex(df['time']).day
my_data=df[["year","month","day", "mag","latitude","longitude"]].sort(["year","month","day"],ascending=[1, 1,1])
print my_data

my_data.to_csv('example.csv')