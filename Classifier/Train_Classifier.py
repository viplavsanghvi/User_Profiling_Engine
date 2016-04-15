import sklearn
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier 


if __name__=="__main__":
	#'items_clicks_feature.csv',
#'items_duration_feature.csv',
#'items_month_feature.csv',
#'items_day_of_month_feature.csv',
#'items_week_hour_feature.csv',
#'items_day_hour_feature.csv',
#'items_day_of_week_feature.csv'
#'items_popularity_feature.csv',
	data=pd.read_csv('../Feature_Extraction/Train_Files/items_buys_per_clicks_feature.csv')
	data['clicks']=pd.read_csv('../Feature_Extraction/Train_Files/items_clicks_feature.csv')
	#data['day-of-month']=pd.read_csv('../Feature_Extraction/Train_Files/items_day_of_month_feature.csv')
	#data['day-of-week']=pd.read_csv('../Feature_Extraction/Train_Files/items_day_of_week_feature.csv')
	#data['duration']=pd.read_csv('../Feature_Extraction/Train_Files/items_duration_feature_int.csv')
	#data['day-hour']=pd.read_csv('../Feature_Extraction/Train_Files/items_day_hour_feature.csv')
	#data['month']=pd.read_csv('../Feature_Extraction/Train_Files/items_month_feature.csv')
	#data['popular']=pd.read_csv('../Feature_Extraction/Train_Files/items_popularity_feature.csv')
	print(data.shape)
	labels=pd.read_csv('../Feature_Extraction/Train_Files/items_labelled_file.csv')

	rf=RandomForestClassifier(n_estimators=10,n_jobs=2,class_weight='subsample')
	rf.fit(data, labels)
	joblib.dump(rf, '../pickle/trained_rf.pickle')
