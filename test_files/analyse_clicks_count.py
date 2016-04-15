import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

clicks = pd.read_csv("../data/yoochoose-clicks1.dat", 
                   names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})


clicks=clicks[['session','item','timestamp']].groupby(['session','item']).count()

clicks.columns=["clicks-cnt"]
clicks.to_csv('items_clicks_feature.csv',index=False)

