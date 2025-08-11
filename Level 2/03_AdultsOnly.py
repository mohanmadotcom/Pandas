# Program: AdultsOnly (Pure Python)
data = [
    {"user_id": 1, "name": "Alice", "age": 17},
    {"user_id": 2, "name": "Bob", "age": 25},
    {"user_id": 3, "name": "Charlie", "age": 18}
]

result = [{"user_id": d["user_id"], "name": d["name"]} for d in data if d["age"] >= 18]

for r in result:
    print(r)
