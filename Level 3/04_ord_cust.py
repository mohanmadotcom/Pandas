# Python (pandas)
import pandas as pd
orders = pd.DataFrame([{"order_id":1,"customer_id":"C1","amount":100.0},
                       {"order_id":2,"customer_id":"C2","amount":50.0}])
customers = pd.DataFrame([{"customer_id":"C1","name":"Alice"},
                          {"customer_id":"C3","name":"Charlie"}])
print(pd.merge(orders, customers, on="customer_id", how="inner")[["order_id","name","amount"]])
