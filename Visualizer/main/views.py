from django.shortcuts import render
import plotly.express as px
import pandas as pd
import os

DIRECTORY = os.getcwd()

def visualization(request):
    """Read the .csv data from the data directory, then build/render the graph."""
    os.chdir('..')
    current_directory = os.getcwd()
    file = pd.read_csv(f'{current_directory}/data/friday.csv')
    headers = ['Date', 'Time', 'Day', 'Occupancy (%)']
    file.to_csv(f'{current_directory}/data/friday.csv', header=headers, index=False)
    df = pd.read_csv(f'{current_directory}/data/friday.csv')
    os.chdir(DIRECTORY)

    fig = px.line(df, x='Time', y='Occupancy (%)', title=f"{df['Day'].values[0]}'s Occupancy Trend")
    fig.update_yaxes(range = [0,120])
    fig.update_layout(
        paper_bgcolor = '#003262',
        font_color = '#FDB515'
    )
    graph = fig.to_html()
    return render(request, 'visualization.html', context={'graph': graph})
  
def insights(request):
    return render(request, 'insights.html')