from bokeh.io import output_file, show
from bokeh.plotting import figure

plot = figure()
plot.circle(x=10, y=[2,5,8,12], size=[10, 20, 30, 40])
#output_file('circle demo.html')
show(plot)