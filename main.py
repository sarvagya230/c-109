import csv
import statistics
import pandas
import plotly.figure_factory as ff
df=pandas.read_csv("data.csv")
data=df["math score"].to_list()
fig=ff.create_distplot([data],["math score"],colors=["#00c8c8"])
fig.update_layout({
    'paper_bgcolor':'#fff',
    "plot_bgcolor":'#fff',
})

fig.show()
print(data)


