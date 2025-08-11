import pandas as pd

# Sample data with duplicates
data = [("Alice", 25), ("Bob", 32), ("Alice", 25)]
df = pd.DataFrame(data, columns=["name", "age"])

# Show original data
print("Original DataFrame:")
print(df)

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

# Show result
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)
