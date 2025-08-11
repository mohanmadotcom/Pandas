# Program: ExpensiveItems (Pure Python)
data = [
    {"item_id": 1, "item_name": "Chair", "price": 75},
    {"item_id": 2, "item_name": "Table", "price": 150},
    {"item_id": 3, "item_name": "Lamp", "price": 120}
]

result = [{"item_id": d["item_id"], "item_name": d["item_name"]}
          for d in data if d["price"] > 100]

for r in result:
    print(r)
