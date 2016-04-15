import pandas as pd
import numpy as np

clicks = pd.read_csv("../data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

buys = pd.read_csv("../data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])

clicks=clicks[['session','item','timestamp']].groupby(['session','item'],as_index=False).min()


buys=buys[['session','item','timestamp']].groupby(['session','item'],as_index=False).min()
buys['label']=1
# print buys.head()


# clicks=pd.merge(clicks,buys,on=['session','item'],how='inner')
clicks=pd.merge(clicks,buys,on=['session','item'],how='outer')
clicks.fillna(value=0,inplace=True)
clicks=clicks[['label']]
clicks.to_csv('items_labels.csv',index=False)