# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"dt":"2025-08-01","amount":100.0},
    {"dt":"2025-08-02","amount":200.0},
    {"dt":"2025-08-03","amount":50.0},
    {"dt":"2025-08-04","amount":150.0}
])
df["dt"] = pd.to_datetime(df["dt"])
df = df.sort_values("dt")
df["3day_avg"] = df["amount"].rolling(window=3, min_periods=1).mean()
print(df)
