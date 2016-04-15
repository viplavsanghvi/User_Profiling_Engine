import pandas as pd
import numpy as np
import matplotlib as mpl
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.externals import joblib
# TEST_DATA_PATH="test_files/"
# def iter_corpus(files=[],path=""):
# 	result=pd.DataFrame()
# 	for i in files:
# 		temp=pd.read_csv(path+i)
# 		result[temp.columns]=temp[temp.columns]
# 	return result


# test=iter_corpus(['items_clicks_feature.csv','items_buys_per_clicks_feature_mod.csv','items_day_hour_mod_feature.csv','items_popularity_feature.csv'],path=TEST_DATA_PATH)
# '','','','items_day_hour_feature.csv','','items_popularity_feature.csv'
test=pd.read_csv('../test_files/test_features/items_buys_per_clicks_feature_mod.csv')
test['clicks']=pd.read_csv('../test_files/test_features/items_clicks_feature.csv')
# test['day-of-month']=pd.read_csv('../test_files/test_features/items_day_of_month_feature.csv')
# test['day-of-week']=pd.read_csv('../test_files/test_features/items_day_of_week_feature.csv')
# test['duration']=pd.read_csv('../test_files/test_features/items_duration_feature_int.csv')
test['day-hour']=pd.read_csv('../test_files/test_features/items_day_hour_mod_feature.csv')
test['month']=pd.read_csv('../test_files/test_features/items_month_feature.csv')
test['popular']=pd.read_csv('../test_files/test_features/items_popularity_feature.csv')
print(test.shape)
rf=joblib.load('../pickle/rf_1+2+6+8+7_10/trained_rf.pickle')
results=rf.predict(test)
print results

np.savetxt("./"+"session_labelled_file_our.csv",results,delimiter='\n',header='Label',fmt='%d')
test_session_item=pd.read_csv('../data/test_session_item.csv')
test_labels = pd.read_csv('../data/true_labels.csv')

def score(test_session_item,true_labels,predicted_labels):
    session_item=pd.DataFrame(test_session_item)
    total_sessions=session_item['session'].unique()
    total_sessions_no=len(total_sessions)
    session_item['true']=true_labels
    session_item['predicted']=predicted_labels
    true_var=session_item[session_item['true']>0][['session','item']]
    predicted_var=session_item[session_item['predicted']>0][['session','item']]
    true_var=true_var.groupby(['session'])
    predicted_var=predicted_var.groupby(['session'])
    true_dict=true_var.groups
    predicted_dict=predicted_var.groups
    buys_sessions_no=len(true_dict)
    fraction=buys_sessions_no/total_sessions_no
    ans=0
    for i in predicted_dict:
        pred_key=i
        pred_val=np.array(predicted_dict[pred_key])
        if pred_key not in true_dict:
            ans-=fraction
        else:
            ans+=fraction
            true_val=np.array(true_dict[pred_key])
            ans+=len(np.intersect1d(pred_val,true_val))/len(np.union1d(pred_val,true_val))
    return ans
            
        
    


x=score(test_session_item.copy(),test_labels,results)
print(x)