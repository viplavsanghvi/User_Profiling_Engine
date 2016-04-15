import pandas as pd
import numpy as np
import matplotlib as mpl
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.externals import joblib

month_cat_1=[4,5]
month_cat_2=[6,8]
month_cat_3=[7,9]


day_week_cat_1=[0,2,3,4]
day_week_cat_2=[1]
day_week_cat_3=[5,6]

day_month_cat_1=[6,12,21,31]
day_month_cat_2=[1,3,4,5,7,9,10,11,13,14,16,17,18,19,22,23,24,26]
day_month_cat_3=[2,8,15,20,25,27,30]
day_month_cat_4=[28,29]


hour_cat_1=[0,1,2,3,4,5]
hour_cat_2=[6,21,22,23]
hour_cat_3=[7,8,9,10,11,12,13,14,15,16,17,18,19,20]

popular_items=pd.read_csv("../final_features/top_popular_item_feature.csv",names=['item'])
popular_items.set_index('item',inplace=True)

top_buys_per_clicks=pd.read_csv("../final_features/clicks_and_buys_feature.csv",names=['item'])
top_buys_per_clicks.set_index('item',inplace=True)


def extract_month(x):
	x=x.month
	if x in month_cat_1:
		return 1
	elif x in month_cat_2:
		return 2
	elif x in month_cat_3:
		return 3

def extract_day_of_week(x):
	x=x.dayofweek
	if x in day_week_cat_1:
		return 1
	elif x in day_week_cat_2:
		return 2
	elif x in day_week_cat_3:
		return 3
	# return x.month

def extract_hour(x):
	x=x.hour
	if x in hour_cat_1:
		return 1
	elif x in hour_cat_2:
		return 2
	elif x in hour_cat_3:
		return 3

def extract_day_of_month(x):
	x=x.day
	if x in day_month_cat_1:
		return 1
	elif x in day_month_cat_2:
		return 2
	elif x in day_month_cat_3:
		return 3
	elif x in day_month_cat_4:
		return 4

def extract_popular_items(x):
	if x in popular_items.index:
		return 1
	else:
		return 0

def extract_top_buys_clicks_items(x):
	if x in top_buys_per_clicks.index:
		return 1
	else:
		return 0

clicks = pd.read_csv("../data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

buys = pd.read_csv("../data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])

clicks=clicks[['session','item','timestamp']].groupby(['session','item'],as_index=False).min()
print clicks['item'].head()

buys=buys[['session','item']].drop_duplicates()
buys['label']='Y'
# print buys.head()


# clicks=pd.merge(clicks,buys,on=['session','item'],how='inner')
clicks=pd.merge(clicks,buys,on=['session','item'],how='outer')
clicks.fillna(value='N',inplace=True)


clicks['month']=clicks['timestamp'].apply(extract_month)
clicks['dayofweek']=clicks['timestamp'].apply(extract_day_of_week)
clicks['hour']=clicks['timestamp'].apply(extract_hour)
clicks['dayofmonth']=clicks['timestamp'].apply(extract_day_of_month)
clicks['popular']=clicks['item'].apply(extract_popular_items)
clicks['buysperclick']=clicks['item'].apply(extract_top_buys_clicks_items)
clicks['duration']=pd.read_csv('items_duration_feature.csv')
clicks['clicks_cnt']=pd.read_csv('items_clicks_feature.csv')
target=np.array(clicks['label']).tolist()
#clicks=clicks[['item','month','dayofweek','hour','dayofmonth','popular','buysperclick']].set_index('item')



clicks.to_csv('clean_all.csv')

