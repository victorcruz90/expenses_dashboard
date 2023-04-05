from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd



def render(app: Dash, data: pd) -> html.Div:
    @app.callback(
        Output('bar-chart', 'children'),
        Input('expenses', 'data')
        )
    def update_graph(rows):

        #filtering the data
        data = pd.DataFrame(rows, columns=['Date', 'Category', 'Amount'])
        data['Date'] = pd.to_datetime(data['Date'])
        data1 = data.groupby([pd.Grouper(key='Date', freq='2W-WED', closed='left', label='left'), "Category"]).sum(numeric_only=True).reset_index()


        #Ploting the graph
        fig = px.histogram(data1, x='Date', y='Amount',color='Category', color_discrete_sequence=px.colors.sequential.thermal, text_auto=True)
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)', 
            bargap=0.3,
            xaxis_title_text='Fornight pay date', 
            yaxis_title_text='Total',
            font_family='Arial',
            xaxis=dict(tickmode='array', tickvals= data1['Date'], ticktext = data1['Date'].apply(lambda x: x.strftime('%d-%b-%Y')),automargin=True),
            ),
        fig.update_yaxes(showgrid=False)
        # fig.update_traces(xbins_size='')
        fig.update_xaxes(type='category')
        return html.Div(children=dcc.Graph(figure=fig), id='bar-chart')
    


    return html.Div(id='bar-chart')
   
