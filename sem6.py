import pandas as pd

d = {
    'one': pd.Series([1, 2, 3], index=['A', 'B', 'C']),
    'two': pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
}

df = pd.DataFrame(d)
print(df)
print(df.shape)
print(df.columns)
print(df.iterrows())
print(df.index)