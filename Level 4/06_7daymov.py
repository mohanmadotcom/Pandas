# pandas_task6.py
from pandas_setup import order_items
import pandas as pd
daily = (order_items[~order_items['is_returned']]
         .groupby('order_date')['price'].sum().reset_index().sort_values('order_date'))
daily['rolling_7d_avg'] = daily['price'].rolling(window=7, min_periods=1).mean()
print(daily)
