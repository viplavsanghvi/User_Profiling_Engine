import pandas as pd
import numpy as np
import matplotlib as mpl

def extract_day(x):
    return x.dayofweek

clicks = pd.read_csv("../data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

clicks=clicks[['session','item','timestamp']].groupby(['session','item']).min()

clicks['timestamp']=clicks['timestamp'].apply(extract_day)

clicks.columns=['day-of-week']

clicks.head()

clicks.to_csv('day_of_week_feature.csv',index=False)

