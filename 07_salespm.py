# pandas_task7.py
from pandas_setup import order_items
import pandas as pd
order_items['ym'] = pd.to_datetime(order_items['order_date']).dt.to_period('M')
pivot = (order_items[~order_items['is_returned']]
         .pivot_table(values='price', index='ym', columns='category', aggfunc='sum').fillna(0))
print(pivot)
