# Sample data as a list of dictionaries
users = [
    {"user_id": 1, "name": "Alice", "is_active": True},
    {"user_id": 2, "name": "Bob", "is_active": False},
    {"user_id": 3, "name": "Charlie", "is_active": True}
]

# Step 1 & 2: Filter users where is_active is True and select user_id and name
active_users = [{"user_id": user["user_id"], "name": user["name"]}
                for user in users if user["is_active"]]

# Step 3: Display the result
for user in active_users:
    print(user)
