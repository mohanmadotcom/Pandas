import pandas as pd

# Sample data
data = [("Alice", 25), ("Bob", 32), ("Charlie", 29), ("David", 40)]
df = pd.DataFrame(data, columns=["name", "age"])

# Show all data
print("Original Data:")
print(df)

# Filter people over age 30
filtered_df = df[df["age"] > 30]

# Show the result
print("\nPeople over age 30:")
print(filtered_df)
