from pandas import Series, DataFrame
import numpy as np

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

print(s1 + s2)

df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

print(df1)
print(df2)

print(df1+df2)                      # number + NaN = NaN
print(df1.add(df2, fill_value=0))   # NaN is replaced with 0

frame = DataFrame(np.arange(12).reshape((4,3)), columns=list('bdc'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)


series = frame.ix['Ohio']       # How to access row
series = frame.ix[0]            # How to access row
col = frame['b']                # How to access column
print(series)

print(frame-series)

series2 = Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)


