from pandas import Series, DataFrame
import numpy as np

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)

new_obj = obj.drop('c')
print(new_obj)

new_obj = obj.drop(['c', 'd'])
print(new_obj)

data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print(data)


data1 = data.drop(['Colorado', 'Ohio'])
print(data1)

data2 = data.drop('two', axis=1)
print(data2)

data3 = data.drop(['two', 'three'], axis=1)
print(data3)
