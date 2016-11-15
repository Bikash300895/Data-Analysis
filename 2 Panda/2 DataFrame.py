from pandas import DataFrame, Series
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)
print(frame)

# Printing a column
print(frame['state'])


frame = DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)

frame1 = DataFrame(data, columns=['year', 'state'])
print(frame1)


frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)


# Printing a row
data = frame2.ix['three']
print(data)


frame2['debt'] = np.arange(5.)
print(frame2)

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)