# pandas_task3.py
from pandas_setup import order_items
import pandas as pd
order_items['ym'] = pd.to_datetime(order_items['order_date']).dt.to_period('M')
monthly = (order_items[~order_items['is_returned']]
           .groupby('ym')['price'].sum().to_frame('monthly_revenue').reset_index())
monthly['prev'] = monthly['monthly_revenue'].shift(1)
monthly['pct_change'] = (monthly['monthly_revenue'] - monthly['prev']) / monthly['prev'] * 100
print(monthly)
