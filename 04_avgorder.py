# pandas_task4.py
from pandas_setup import order_items
ot = (order_items[~order_items['is_returned']]
      .groupby('order_id')['price'].sum().reset_index())
print("avg_order_value:", ot['price'].mean())
