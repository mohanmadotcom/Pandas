# Program: PremiumCustomers (Pure Python)
data = [
    {"customer_id": 1, "name": "Alice", "membership": "Standard"},
    {"customer_id": 2, "name": "Bob", "membership": "Premium"},
    {"customer_id": 3, "name": "Charlie", "membership": "Premium"}
]

result = [{"customer_id": d["customer_id"], "name": d["name"]}
          for d in data if d["membership"] == "Premium"]

for r in result:
    print(r)
