# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"order_id":1,"info":"C1","updated_at":"2025-08-01 10:00:00"},
    {"order_id":1,"info":"C1-updated","updated_at":"2025-08-01 12:00:00"},
    {"order_id":2,"info":"C2","updated_at":"2025-08-02 09:00:00"}
])
df["updated_at"] = pd.to_datetime(df["updated_at"])
df_sorted = df.sort_values(["order_id","updated_at"], ascending=[True, False])
dedup = df_sorted.drop_duplicates(subset=["order_id"], keep="first")
print(dedup)
