import pandas as pd

# Sample data
data = [("Alice", 25, "HR"), ("Bob", 32, "IT"), ("Charlie", 29, "Finance")]
df = pd.DataFrame(data, columns=["name", "age", "department"])

# Show full data
print("Full DataFrame:")
print(df)

# Select only the 'name' and 'department' columns
selected_df = df[["name", "department"]]

# Show result
print("\nSelected Columns:")
print(selected_df)
