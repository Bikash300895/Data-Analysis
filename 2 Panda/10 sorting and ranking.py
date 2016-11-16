from pandas import Series, DataFrame
import numpy as np

obj = Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())

frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                    columns=['d', 'a', 'b', 'c'])

print(frame.sort_index())
print(frame.sort_index(axis=1, ascending=False))

frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)

print(frame.sort_index(by='b'))
print(frame.sort_index(by=['a', 'b']))
