import numpy as np
import pandas as pd

d = {1: 'J', 2: 'a', 3: 'a', 4: 'n'}
p = pd.Series(d, index=[4, 3, 1, 2])
print(p)
p1 = pd.Series(5, index=['a','b','c','d','e'])
print(p1)
