import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_day(x):
    return x.hour

buys = pd.read_csv("./data/popular_item_feature.csv", 
                   names=["item", "click_per_item"])


# print month_of_year_count.sum()
popular_item=buys[buys.click_per_item>=10]
popular_item=popular_item['item']
print popular_item.head(100)
popular_item.to_csv('top_popular_item_feature.csv',index=False)

buys=buys[['click_per_item']]

# buys['timestamp']=buys['timestamp'].apply(extract_day)

# buys.columns=['monthofyear']

buys=buys['click_per_item'].value_counts()


# month_of_year_count=  buys / month_of_year_count 

# print buys

# plt.plot(buys, np.linspace(0,1,buys.size))
buys.plot()
plt.ylabel('Popularity')
plt.show()

# buys.plot.bar()

# plt.show()
