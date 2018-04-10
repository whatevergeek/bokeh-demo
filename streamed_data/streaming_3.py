from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, Select
from bokeh.layouts import layout
from bokeh.plotting import figure
from random import randrange
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from math import radians
from pytz import timezone

#create figure
f=figure(x_axis_type='datetime')

#create webscraping function
def extract_value(currency = "bitcoin"):
    r=requests.get("https://www.investing.com/crypto/" + currency,headers={'User-Agent':'Mozilla/5.0'})

    c=r.content
    soup=BeautifulSoup(c,"html.parser")

    value_raw=soup.findAll("span", {"id": "last_last"})
    float(value_raw[0].text.replace(",", ""))
    value_net=float(value_raw[0].text.replace(",", ""))
    return value_net

#create ColumnDataSource
source=ColumnDataSource(dict(x=[],y=[]))

#create glyphs
f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y',source=source)

#create periodic function
def update():
    new_data=dict(x=[datetime.now(tz=timezone('Asia/Singapore'))],y=[extract_value(select.value)])
    source.stream(new_data,rollover=15)
    print(select.value)
    # print(source.data)

def update_intermediate(attr,old,new):
    source.data=dict(x=[],y=[])
    update()

f.xaxis.formatter=DatetimeTickFormatter(
seconds=["%Y-%m-%d-%H-%M-%S"],
minsec=["%Y-%m-%d-%H-%M-%S"],
minutes=["%Y-%m-%d-%H-%M-%S"],
hourmin=["%Y-%m-%d-%H-%M-%S"],
hours=["%Y-%m-%d-%H-%M-%S"],
days=["%Y-%m-%d-%H-%M-%S"],
months=["%Y-%m-%d-%H-%M-%S"],
years=["%Y-%m-%d-%H-%M-%S"],
)

f.xaxis.major_label_orientation=radians(45)

#create Select widget
options=[("bitcoin","Bitcoin"), ("bitcoin-cash","Bitcoin Cash"),("ethereum","Etherium")]
select=Select(title="Currency",value="bitcoin",options=options)
select.on_change("value",update_intermediate)

#add figure to curdoc and configure callback
lay_out=layout([[f],[select]])
curdoc().add_root(lay_out)
curdoc().add_periodic_callback(update,5000)