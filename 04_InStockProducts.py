# Program: InStockProducts (Pure Python)
data = [
    {"product_id": 101, "product_name": "Pen", "quantity": 0},
    {"product_id": 102, "product_name": "Notebook", "quantity": 20},
    {"product_id": 103, "product_name": "Eraser", "quantity": 5}
]

result = [{"product_id": d["product_id"], "product_name": d["product_name"]}
          for d in data if d["quantity"] > 0]

for r in result:
    print(r)
