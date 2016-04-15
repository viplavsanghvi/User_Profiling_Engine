import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_day(x):
    return x.day

buys = pd.read_csv("../data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])

day_of_month = pd.read_csv("../analysis/day_of_month_feature.csv")

day_of_month_count=day_of_month['dayofmonth'].value_counts()

print day_of_month_count.sum()

buys=buys[['session','timestamp']].groupby(['session']).min()

buys['timestamp']=buys['timestamp'].apply(extract_day)

buys.columns=['dayofmonth']

buys=buys['dayofmonth'].value_counts()

print buys.sum()

day_of_month_count=  buys / day_of_month_count 

print day_of_month_count

day_of_month_count.plot()

plt.show()