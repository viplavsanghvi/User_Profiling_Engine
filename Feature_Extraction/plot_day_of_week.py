import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_day(x):
    return x.dayofweek

buys = pd.read_csv("../data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])

day_of_week = pd.read_csv("../analysis/day_of_week_feature.csv")

day_of_week_count=day_of_week['dayofweek'].value_counts()

print day_of_week_count.sum()

buys=buys[['session','timestamp']].groupby(['session']).min()

buys['timestamp']=buys['timestamp'].apply(extract_day)

buys.columns=['dayofweek']

buys=buys['dayofweek'].value_counts()

print buys.sum()

day_of_week_count=  buys / day_of_week_count 

print day_of_week_count

day_of_week_count.plot()

plt.show()