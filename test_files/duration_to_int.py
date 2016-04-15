import pandas as pd
import numpy as np
import matplotlib as mpl

def convert_to_int(x):
        return int(x)

tmp = pd.read_csv("items_duration_feature.csv")



tmp1=tmp[["duration"]].astype(int)

tmp1.to_csv("'items_duration_int_feature.csv",index=False)
