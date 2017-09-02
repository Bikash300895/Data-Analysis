import numpy as np
from pandas import Series, DataFrame
import pandas as pd

df = pd.read_csv('ex1.csv')
print(df)

# alternative
df = pd.read_table('ex1.csv', sep=',')
print(df)

df = pd.read_csv('ex2.csv', header=None)
print(df)

names = ['a', 'b', 'c', 'd', 'message']
df1 = pd.read_csv('ex2.csv', names=names, index_col='message')
print(df1)

