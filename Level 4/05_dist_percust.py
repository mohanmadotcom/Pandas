# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"order_id":1,"customer_id":"C1","product_id":"P1"},
    {"order_id":2,"customer_id":"C1","product_id":"P2"},
    {"order_id":3,"customer_id":"C1","product_id":"P1"},
    {"order_id":4,"customer_id":"C2","product_id":"P3"}
])
print(df.groupby("customer_id")["product_id"].nunique().reset_index(name="distinct_products"))
