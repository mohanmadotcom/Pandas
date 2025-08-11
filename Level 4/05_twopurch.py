# pandas_task5.py
from pandas_setup import order_items, customers
cat_counts = (order_items[~order_items['is_returned']]
              .groupby('customer_id')['category'].nunique().reset_index().rename(columns={'category':'distinct_cats'}))
res = cat_counts[cat_counts['distinct_cats']>=2].merge(customers, on='customer_id')
print(res)
