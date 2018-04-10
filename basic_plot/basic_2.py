#Task 2: 
# Add additional glyphs (circle)
# Load via pandas
# Add labels

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

#prepare some data
df=pd.read_csv("data.csv")
x=df["x"]
y=df["y"]

#prepare the output file
output_file("temperature.html")

#create a figure object
f=figure()

#Style the plot area
f.plot_width=800
f.plot_height=400
f.background_fill_color="green"
f.background_fill_alpha=0.2

#Style the title
f.title.text="Temperature Tracking"
f.title.text_color="blue"
f.title.text_font="times"
f.title.text_font_size="20px"
f.title.align="center"
f.title.text_alpha = 1

#Style the axes
f.xaxis.minor_tick_line_color="green"
f.yaxis.major_label_orientation="vertical"
f.xaxis.visible=True
f.xaxis.minor_tick_in=-6
f.xaxis.axis_label="Hour"
f.yaxis.axis_label="Temperature"
f.axis.axis_label_text_color="blue"
f.axis.major_label_text_color="green"


#create line plot
f.line(x,y)
f.circle(x,y)


#write the plot in the figure object
show(f)
