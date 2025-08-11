# Program: ActiveSubscriptions (Pure Python)
data = [
    {"user_id": 1, "username": "alice", "is_active": True},
    {"user_id": 2, "username": "bob", "is_active": False},
    {"user_id": 3, "username": "charlie", "is_active": True}
]

result = [{"user_id": d["user_id"], "username": d["username"]}
          for d in data if d["is_active"] == True]

for r in result:
    print(r)
