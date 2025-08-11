# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"order_id":1,"items":[{"item_id":"I1","qty":2},{"item_id":"I2","qty":1}]},
    {"order_id":2,"items":[{"item_id":"I1","qty":3}]}
])
rows = []
for _, r in df.iterrows():
    for it in r["items"]:
        rows.append({"item_id":it["item_id"], "qty":it["qty"]})
flat = pd.DataFrame(rows)
print(flat.groupby("item_id", as_index=False)["qty"].sum().rename(columns={"qty":"total_qty"}))
