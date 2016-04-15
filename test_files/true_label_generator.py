import pandas as pd
import numpy as np

test = pd.read_csv("data/yoochoose-test.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})	

buys=pd.read_csv('./data/correct_solution.csv',names=['session','item','label'])
buys=buys[['session','item','label']].groupby(['session','item'],as_index=False).min()
# print buys.head()
test=test[['session','item','timestamp']].groupby(['session','item'],as_index=False).min()
# print test.head(5)
test=pd.merge(test,buys,on=['session','item'],how='outer')
test.fillna(value=0,inplace=True)
# test=test[['session','item','label']].groupby(['session','item'],as_index=False)
test=test[['label']]
test.to_csv('true_labels.csv',index=False)