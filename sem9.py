import pandas as pd

# Create a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 15, 20, 25, 30, 35]}
df = pd.DataFrame(data)
print(df)
# Group by 'Category'
grouped = df.groupby('Category')

# Calculate the mean value for each group
mean_values = grouped['Value'].mean()

print(mean_values)
