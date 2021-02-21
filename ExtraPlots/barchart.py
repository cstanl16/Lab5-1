import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')


# Sorting values and select first 20 states
df = df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=df['NOC'], y=df['Total'])]

# Preparing layout
layout = go.Layout(title='Total Medals of Olympics 2016 of 20 First top Countries', xaxis_title="Country",
                   yaxis_title="Number of Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
