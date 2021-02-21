import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')


# Preparing data
data = [
    go.Scatter(x=df['average_min_temp'],
            y=df['average_max_temp'],
            text=df['month'],
            mode='markers',
            marker=dict(size=df['record_max_temp_year'] /
100,color=df['record_max_temp_year'] / 100, showscale=True))
]
# Preparing layout
layout = go.Layout(title='Average Min and Max Temp of Each Month', xaxis_title="Average Min Temp",
                   yaxis_title="Average Max Temp", hovermode='closest')

# plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.py')
