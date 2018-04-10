#Task 1: Plot a Basic Line Graph

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x=[1,2,3,4,5] # hour
y=[23,22,24,24,23] # temperature

#prepare the output file
output_file("temperature.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)

#write the plot in the figure object
show(f)
