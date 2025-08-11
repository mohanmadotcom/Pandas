# Python (pandas) — same 10 tasks


# pandas_setup.py (common setup)
import pandas as pd
from datetime import datetime

customers = pd.DataFrame([
    (1, "Alice"),
    (2, "Bob"),
    (3, "Carol"),
    (4, "Dan"),
], columns=["customer_id", "name"])

products = pd.DataFrame([
    (10, "Red T-Shirt", "Apparel"),
    (11, "Blue Jeans", "Apparel"),
    (20, "Coffee Mug", "Home"),
    (21, "Tea Kettle", "Home"),
], columns=["product_id", "product_name", "category"])

orders = pd.DataFrame([
    (1001, 1, "2025-06-01"),
    (1002, 1, "2025-06-03"),
    (1003, 2, "2025-06-10"),
    (1004, 2, "2025-07-01"),
    (1005, 3, "2025-05-15"),
    (1006, 4, "2025-07-10"),
    (1007, 1, "2025-07-11"),
], columns=["order_id", "customer_id", "order_date"])
orders["order_date"] = pd.to_datetime(orders["order_date"]).dt.date

order_items = pd.DataFrame([
    (1001, 10, 2, 20.0, False),
    (1001, 20, 1, 8.0, False),
    (1002, 11, 1, 40.0, True),
    (1003, 10, 3, 20.0, False),
    (1004, 21, 1, 35.0, False),
    (1005, 20, 2, 8.0, False),
    (1006, 11, 1, 40.0, False),
    (1007, 10, 1, 20.0, False),
], columns=["order_id", "product_id", "qty", "unit_price", "is_returned"])
order_items["price"] = order_items["qty"] * order_items["unit_price"]

# enrich
order_items = order_items.merge(products, on="product_id", how="left").merge(orders, on="order_id", how="left")
