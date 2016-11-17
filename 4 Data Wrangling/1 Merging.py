from pandas import Series, DataFrame
import numpy as np
import pandas as pd

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                'data1': range(7)})
print(df1)

df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
print(df2)

print(pd.merge(df1, df2))