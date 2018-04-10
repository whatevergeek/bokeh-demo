#Run in Bokeh Server

#Importing libraries
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource, LabelSet

colormap={'setosa':'red','versicolor':'green','virginica':'blue'}
flowers['color']=[colormap[x] for x in flowers['species']]
flowers['sepal_width_scaled']=flowers['sepal_width']*4

urlmap={'setosa':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/800px-Kosaciec_szczecinkowaty_Iris_setosa.jpg',
        'versicolor':'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/800px-Blue_Flag%2C_Ottawa.jpg',
        'virginica':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/800px-Iris_virginica.jpg'}
flowers['imgs']=[urlmap[x] for x in flowers['species']]

setosa=ColumnDataSource(flowers[flowers["species"]=="setosa"])
versicolor=ColumnDataSource(flowers[flowers["species"]=="versicolor"])
virginica=ColumnDataSource(flowers[flowers["species"]=="virginica"])

#Create the figure object
f=figure()

#adding glyphs
f.circle(x="petal_length", y="petal_width", size="sepal_width_scaled",
         fill_alpha=0.2,color="color",line_dash=[5,3],legend='Setosa', source=setosa)

f.circle(x="petal_length", y="petal_width", size="sepal_width_scaled",
         fill_alpha=0.2,color="color",line_dash=[5,3],legend='Versicolor', source=versicolor)

f.circle(x="petal_length", y="petal_width", size="sepal_width_scaled",
         fill_alpha=0.2,color="color",line_dash=[5,3],legend='Virginica', source=virginica)


#Style the tools
f.tools=[PanTool(),ResetTool()]
hover=HoverTool(tooltips="""
     <div>
            <div>
                <img
                    src="@imgs" height="42" alt="@imgs" width="42"
                    style="float: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
            <div>
                <span style="font-size: 15px; font-weight: bold;">@species</span>
            </div>
            <div>
                <span style="font-size: 10px; color: #696;">Petal length: @petal_length</span><br>
                <span style="font-size: 10px; color: #696;">Petal width: @petal_width</span>
            </div>
        </div>
""")
f.add_tools(hover)
f.toolbar_location='above'
f.toolbar.logo=None

#Style the legend
f.legend.location=(10,450)
f.legend.background_fill_alpha=0
f.legend.border_line_color=None
f.legend.margin=10
f.legend.padding=18
f.legend.label_text_color='olive'
f.legend.label_text_font='times'


#create layout and add to curdoc
curdoc().add_root(f)