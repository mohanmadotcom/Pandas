# pandas_task10.py
from pandas_setup import order_items
import pandas as pd
daily = (order_items[~order_items['is_returned']]
         .groupby(['product_id','order_date'])['price'].sum().reset_index().rename(columns={'price':'daily_rev'}))
# compute z-score per product
def flag_anomalies(df):
    mu = df['daily_rev'].mean()
    sigma = df['daily_rev'].std(ddof=0)
    df['z'] = (df['daily_rev'] - mu) / (sigma if sigma!=0 else 1)
    return df[df['z'].abs() > 3]
anoms = daily.groupby('product_id').apply(flag_anomalies).reset_index(drop=True)
print(anoms)
