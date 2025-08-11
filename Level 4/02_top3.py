# pandas_task2.py
from pandas_setup import order_items
rev = (order_items[~order_items["is_returned"]]
       .groupby(["customer_id","product_id","product_name"], as_index=False)["price"]
       .sum().rename(columns={"price":"revenue"}))
rev['rank'] = rev.groupby('customer_id')['revenue'].rank(method='dense', ascending=False)
print(rev[rev['rank']<=3].sort_values(['customer_id','rank']))
