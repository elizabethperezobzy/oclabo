import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, None, 4, 5],
        'B': [None, 2, 3, None, 5],
        'C': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Calculate the percentage of missing values for each column
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)
