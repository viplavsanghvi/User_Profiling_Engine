import pandas as pd
import numpy as np
import matplotlib as mpl

def extract_month(x):
    return x.month

clicks = pd.read_csv("../data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

clicks=clicks[['session','item','timestamp']].groupby(['session','item']).min()

clicks['timestamp']=clicks['timestamp'].apply(extract_month)

clicks.columns=['monthofyear']

print clicks.head()

clicks.to_csv('month_of_year_feature.csv',index=False)
