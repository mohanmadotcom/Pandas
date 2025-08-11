# Python (pandas)
import pandas as pd
df = pd.DataFrame([
    {"region":"North","product":"P1","amount":100.0},
    {"region":"North","product":"P2","amount":50.0},
    {"region":"South","product":"P1","amount":70.0}
])
print(df.pivot_table(index="region", columns="product", values="amount", aggfunc="sum").reset_index())
