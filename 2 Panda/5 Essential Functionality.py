from pandas import Series, DataFrame

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

obj3 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj3)