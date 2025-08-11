# pandas_task1.py
from pandas_setup import order_items, customers
res = (order_items[~order_items["is_returned"]]
       .groupby("customer_id", as_index=False)["price"]
       .sum()
       .rename(columns={"price":"total_sales"}))
res = res.merge(customers, on="customer_id")
res = res.sort_values("total_sales", ascending=False)
print(res)
