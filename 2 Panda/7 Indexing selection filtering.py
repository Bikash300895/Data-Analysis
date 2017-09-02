from pandas import Series, DataFrame
import numpy as np

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)

print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'c', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])
print(obj['b':'d'])

obj['b':'c'] = 5
print(obj)


data = DataFrame(np.arange(16).reshape((4, 4)),
                index =['Ohio', 'Colorado', 'Utah', 'New York'],
                columns =['one', 'two', 'three', 'four'])

print(data)

print(data['two'])
print(data[['three', 'one']])
print(data[:2])
print(data[data['three'] > 5])

print(data < 5)

data1 = data[data < 5] = 0
print(data1)

print(data.ix['Colorado', ['two', 'three']])
print(data.ix[['Colorado', 'Utah'], [3, 0, 1]])

