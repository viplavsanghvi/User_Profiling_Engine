import pandas as pd
import numpy as np
import matplotlib as mpl

clicks = pd.read_csv("data/yoochoose-clicks.dat", 
                     names=["session", "timestamp", "item", "category"], 
                     parse_dates=["timestamp"],
                     converters={"category": lambda c: -1 if c == "S" else c})

buys = pd.read_csv("data/yoochoose-buys.dat", 
                   names=["session", "timestamp", "item", "price", "qty"], 
                   parse_dates=["timestamp"])

print "Number of sessions in clicks"
print len(clicks['session'].unique())

print "Number of sessions in buys"
print len(buys['session'].unique())
