from bokeh.models import ColumnDataSource

source = ColumnDataSource(data={
    'x': [1,2,3,4,5],
    'y': [8,6,5,2,3]
})

print(source.data)