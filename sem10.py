import pandas as pd

# Creating two DataFrames with the same index
df1 = pd.DataFrame({'value': [1, 2, 3, 4]}, index=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame({'value': [5, 6, 7, 8]}, index=['B', 'D', 'E', 'F'])

# Performing a join based on the index
joined_df = df1.join(df2, how='inner', lsuffix='_df1', rsuffix='_df2')

print(joined_df)
