from bokeh.io import output_file, show
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [8, 6, 5, 2, 3]

plot = figure()
plot.line(x, y, line_width=2)
plot.circle(x,y,fill_color='white', size=10)

output_file('lines.html')
show(plot)