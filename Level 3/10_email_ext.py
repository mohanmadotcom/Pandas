# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"user_id":1,"email":"alice@gmail.com"},
    {"user_id":2,"email":"bob@yahoo.com"},
    {"user_id":3,"email":"charlie@gmail.com"}
])
df["domain"] = df["email"].str.extract(r'@([^@]+)$', expand=False)
print(df.groupby("domain", as_index=False)["user_id"].count().rename(columns={"user_id":"user_count"}))
