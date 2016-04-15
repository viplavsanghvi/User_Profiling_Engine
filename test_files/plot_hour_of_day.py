import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_day(x):
    return x.hour

buys = pd.read_csv("../data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])

hour_of_day = pd.read_csv("../analysis/hour_of_day_feature.csv")

hour_of_day_count=hour_of_day['hourofday'].value_counts()

print hour_of_day_count.sum()

buys=buys[['session','timestamp']].groupby(['session']).min()

buys['timestamp']=buys['timestamp'].apply(extract_day)

buys.columns=['hourofday']

buys=buys['hourofday'].value_counts()

print buys.sum()

hour_of_day_count=  buys / hour_of_day_count 

print hour_of_day_count

hour_of_day_count.plot()

plt.show()