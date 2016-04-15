import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

clicks = pd.read_csv("../data/yoochoose-clicks1.dat", 
                   names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})


clicks=clicks[['session','item','timestamp']].groupby(['session','item'])

min_ts=clicks.min()
max_ts=clicks.max()

session_duration=max_ts - min_ts
session_duration.columns=["duration"]

# print session_duration.head(100)

#print session_duration.describe()

session_duration_min=session_duration['duration'] / np.timedelta64(1, 'm')
session_duration_min.to_csv('items_duration_feature.csv',index=False)
#sns.kdeplot(session_duration_sec[(session_duration_sec < 1000) & (session_duration_sec > 0)]);
#plt.show()
