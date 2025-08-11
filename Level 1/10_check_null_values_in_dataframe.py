import pandas as pd

# Sample data with a missing value
data = [("Alice", 25), ("Bob", None), ("Charlie", 29)]
df = pd.DataFrame(data, columns=["name", "age"])

# Show original data
print("Original DataFrame:")
print(df)

# Check for null values
print("\nCheck for null values in each column:")
print(df.isnull())

# Count total nulls per column
print("\nTotal nulls per column:")
print(df.isnull().sum())
