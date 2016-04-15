import pandas as pd
import numpy as np
import matplotlib as mpl

clicks = pd.read_csv("./data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

buys = pd.read_csv("./data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])

clicks=clicks[['item']]
clicks_cnt=clicks['item'].value_counts()
clicks_cnt=pd.DataFrame(clicks_cnt).reset_index()
# print clicks_cnt
clicks_cnt.columns=['item','clicks_cnt']
# clicks_cnt.set_index('item',inplace=True)

buys=buys[['item']]
buys_cnt=buys['item'].value_counts()
buys_cnt=pd.DataFrame(buys_cnt).reset_index()
buys_cnt.columns=['item','buys_cnt']
# buys_cnt.set_index('item',inplace=True)

print clicks_cnt.head()

print buys_cnt.head()

clicks=pd.merge(clicks_cnt,buys_cnt,on=['item'],how='inner')
clicks['buys_per_click']=clicks['buys_cnt']/clicks['clicks_cnt']
clicks=clicks[['item','buys_per_click']]
clicks=clicks.sort(['buys_per_click'], ascending=False)
print clicks.head()
# clicks=clicks[['session_item','clicks','buys']]
i=len(clicks)/4
clicks=clicks[['item']].head(i)
clicks.to_csv('clicks_and_buys_feature.csv',index=False)

