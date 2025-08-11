# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"order_id":1,"product_id":"P1","quantity":2,"price":10.0},
    {"order_id":2,"product_id":"P2","quantity":1,"price":20.0},
    {"order_id":3,"product_id":"P1","quantity":3,"price":10.0},
    {"order_id":4,"product_id":"P3","quantity":5,"price":5.0}
])
df["sale"] = df["quantity"] * df["price"]
print(df.groupby("product_id", as_index=False)["sale"].sum().rename(columns={"sale":"total_sales"}))
