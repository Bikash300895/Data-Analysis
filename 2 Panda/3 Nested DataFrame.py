from pandas import DataFrame, Series

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame = DataFrame(pop)
print(frame)

frame = frame.T
print(frame)