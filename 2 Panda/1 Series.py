from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 7, -5, 3])
print(obj)

print(obj.values)
print(obj.index)

obj = Series([4, 7, -5, 3], index=['b', 'd', 'a', 'c'])
print(obj)

print(obj['a'])

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj = Series(sdata)
print(obj)


states = ['California', 'Ohio', 'Oregon', 'Texas']
obj = Series(sdata, index=states)
print(obj)

print(obj.isnull())

