import pandas as pd

# Sample data
data = [("Alice", 25), ("Bob", 32)]
df = pd.DataFrame(data, columns=["name", "age"])

# Rename column 'name' to 'full_name'
df_renamed = df.rename(columns={"name": "full_name"})

# Show result
print("DataFrame with renamed column:")
print(df_renamed)
