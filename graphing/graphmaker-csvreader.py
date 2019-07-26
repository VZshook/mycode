import plotly.express as px
gapminder = px.data.gapminder().query("year == 2007")
fig = px.line_geo(gapminder, locations="iso_alpha", 
                  color="continent", # "continent" is one of the columns of gapminder 
                  projection="orthographic")
fig.show()
