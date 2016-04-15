import pandas as pd
import numpy as np
import matplotlib as mpl

def extract_hour(x):
    return x.hour

clicks = pd.read_csv("../data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

clicks=clicks[['session','item','timestamp']].groupby(['session','item']).min()

clicks['timestamp']=clicks['timestamp'].apply(extract_hour)

clicks.columns=['hour-of-day']

print clicks.head()

clicks.to_csv('hour_of_day_feature.csv',index=False)

