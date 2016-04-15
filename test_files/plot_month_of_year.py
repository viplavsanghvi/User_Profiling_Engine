import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_day(x):
    return x.hour

buys = pd.read_csv("../data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])

month_of_year = pd.read_csv("../analysis/month_of_year_feature.csv")

month_of_year_count=month_of_year['monthofyear'].value_counts()

print month_of_year_count.sum()

buys=buys[['session','timestamp']].groupby(['session']).min()

buys['timestamp']=buys['timestamp'].apply(extract_day)

buys.columns=['monthofyear']

buys=buys['monthofyear'].value_counts()

print buys.sum()

month_of_year_count=  buys / month_of_year_count 

print month_of_year_count

month_of_year_count.plot()

plt.show()