import pandas as pd

# Sample data
data = [("Alice", 25), ("Bob", 32), ("Charlie", 29)]
df = pd.DataFrame(data, columns=["name", "age"])

# Sort the DataFrame by age in ascending order
sorted_df = df.sort_values(by="age")

# Show result
print("Data sorted by age:")
print(sorted_df)
