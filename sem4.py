import numpy as np
import random
import pandas as pd
s=pd.Series(np.random.random(5),index=['a','b','c','d','e'])
print(s)
print(type(s))
print(s.index)
print(s.values)