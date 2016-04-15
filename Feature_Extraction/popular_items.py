import pandas as pd
import numpy as np

popular_items=pd.read_csv("./data/top_popular_item_feature.csv",names=['item'])
popular_items.set_index('item',inplace=True)


def extract_popular_items(x):
	if x in popular_items.index:
		return 1
	else:
		return 0

clicks = pd.read_csv("./data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})


clicks=clicks[['session','item','timestamp']].groupby(['session','item'],as_index=False)
print clicks['item'].head()

clicks['popular']=clicks['item'].apply(extract_popular_items)


clicks=clicks[['popular']]
clicks.to_csv('item_popularity_feature.csv',index=False)

