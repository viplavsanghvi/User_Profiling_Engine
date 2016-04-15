import pandas as pd
import numpy as np
import matplotlib as mpl


buys = pd.read_csv("../data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])


buys=buys[['item']]
# buys=buys.set_index('item')
buys_count=buys['item'].value_counts()
print buys_count
buys_count.to_csv('popular_item_feature.csv')
print buys_count
