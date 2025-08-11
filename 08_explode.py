# pandas_task8.py
import pandas as pd
from pandas_setup import customers
# create orders_with_items like PySpark example
orders_with_items = pd.DataFrame([
    (5001, 1, [{'product_id':10,'qty':1,'unit_price':20.0},{'product_id':20,'qty':2,'unit_price':8.0}]),
    (5002, 2, [{'product_id':11,'qty':1,'unit_price':40.0}]),
], columns=['order_id','customer_id','items'])
exploded = orders_with_items.explode('items')
exploded = pd.concat([exploded.drop(['items'], axis=1), exploded['items'].apply(pd.Series)], axis=1)
exploded['price'] = exploded['qty'] * exploded['unit_price']
agg = exploded.groupby('product_id')['price'].sum().reset_index().rename(columns={'price':'total_revenue'})
print(agg)
