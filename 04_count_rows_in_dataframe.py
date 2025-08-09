import pandas as pd

# Sample data
data = [("Alice", 25), ("Bob", 32), ("Charlie", 29), ("David", 40)]
df = pd.DataFrame(data, columns=["name", "age"])

# Show the data
print("Data:")
print(df)

# Count number of rows
row_count = len(df)

print(f"\nNumber of rows: {row_count}")
