from pandas import Series, DataFrame

obj = Series(range(3), index=['a', 'b', 'c'])
print(obj)

index = obj.index
print(index)
