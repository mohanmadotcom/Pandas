# pandas_task9.py
from pandas_setup import orders, customers
import pandas as pd
today = pd.to_datetime("2025-08-10").date()
last_order = orders.groupby('customer_id')['order_date'].max().reset_index()
last_order['days_since'] = last_order['order_date'].apply(lambda d: (today - d).days)
churned = last_order[last_order['days_since'] > 90].merge(customers, on='customer_id')
print(churned)
