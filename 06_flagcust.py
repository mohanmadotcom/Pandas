# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"order_id":1,"customer_id":"C1","order_date":"2025-08-01"},
    {"order_id":2,"customer_id":"C1","order_date":"2025-08-05"},
    {"order_id":3,"customer_id":"C2","order_date":"2025-08-03"}
])
df["order_date"] = pd.to_datetime(df["order_date"])
first = df.groupby("customer_id")["order_date"].transform("min")
df["is_repeat"] = df["order_date"] > first
print(df.sort_values("order_id"))
