from pandas import Series, DataFrame
import numpy as np

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)

new_obj = obj.drop('c')
print(new_obj)

new_obj = obj.drop(['c', 'd'])
print(new_obj)