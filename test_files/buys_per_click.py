import pandas as pd
import numpy as np

top_buys_per_clicks=pd.read_csv("../final_features/clicks_and_buys_feature.csv",names=['item'])
top_buys_per_clicks.set_index('item',inplace=True)


def extract_top_buys_clicks_items(x):
	if x in top_buys_per_clicks.index:
		return 1.0
	else:
		return 0.0

clicks = pd.read_csv("./data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})


clicks=clicks[['session','item','timestamp']].groupby(['session','item'],as_index=False)
print clicks['item'].head()

clicks['mod-ratio']=clicks['item'].apply(extract_top_buys_clicks_items)


clicks=clicks[['mod-ratio']]
clicks.to_csv('buys_per_click_feature.csv',index=False)

