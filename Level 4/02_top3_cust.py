# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"order_id":1,"customer_id":"C1","amount":100.0},
    {"order_id":2,"customer_id":"C2","amount":50.0},
    {"order_id":3,"customer_id":"C1","amount":30.0},
    {"order_id":4,"customer_id":"C3","amount":200.0},
    {"order_id":5,"customer_id":"C2","amount":120.0}
])
agg = df.groupby("customer_id", as_index=False)["amount"].sum().rename(columns={"amount":"total"})
print(agg.sort_values("total", ascending=False).head(3))
