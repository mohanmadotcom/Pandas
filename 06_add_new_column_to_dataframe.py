import pandas as pd

# Sample data
data = [("Alice", 25), ("Bob", 32), ("Charlie", 29)]
df = pd.DataFrame(data, columns=["name", "age"])

# Add a new column 'country' with a default value
df["country"] = "India"

# Show result
print("DataFrame with new column:")
print(df)
