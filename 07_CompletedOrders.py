# Program: CompletedOrders (Pure Python)
data = [
    {"order_id": 1, "customer": "Alice", "status": "Pending"},
    {"order_id": 2, "customer": "Bob", "status": "Completed"},
    {"order_id": 3, "customer": "Charlie", "status": "Completed"}
]

result = [{"order_id": d["order_id"], "customer": d["customer"]}
          for d in data if d["status"] == "Completed"]

for r in result:
    print(r)
