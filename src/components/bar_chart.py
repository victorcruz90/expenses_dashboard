from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
from datetime import datetime as dt
import pandas as pd



def render(app: Dash, data: pd) -> html.Div:
    fig = px.histogram(data, x='Date', y='Amount',color='Category', )
    fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)', 
            bargap=0.3, 
            xaxis_title_text='Fornight start date', 
            yaxis_title_text='Total',
            font_family='Arial'
        ),
    fig.update_yaxes(showgrid=False)
    fig.update_xaxes(categoryorder='total ascending', mirror=True)

    return html.Div(id='bar-graph', children=[dcc.Graph(figure=fig)])
   
