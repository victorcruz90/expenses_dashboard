from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd



def render(app: Dash, data: pd) -> html.Div:
    @app.callback(
        Output('bar-chart', 'children'),
        Input('expenses', 'data'),
        Input('fortnight-dropdown', 'value'),
        State('expenses', 'data')
        )
    def update_graph(rows, fortnight_values: list, data_state):

        #Grouping the data
        # data = pd.DataFrame(rows)
        data['Date'] = pd.to_datetime(data['Date'])
        data1= data.query('Amount <= 0').copy()
        data1['Amount'] = data1['Amount'].abs()
        data1 = data1.groupby([pd.Grouper(key='Date', freq='2W-WED', closed='left', label='left'), "Category"]).sum(numeric_only=True).reset_index()

        #Filtering the data
        if fortnight_values: 
            data2 = data1.query('Date in @fortnight_values')
            # data2 = data2.set_index('Date')
            #Ploting the graph
            fig = px.histogram(data2, x='Date', y='Amount',color='Category', color_discrete_sequence=px.colors.qualitative.Dark24, text_auto='.2f')
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', 
                bargap=0.3,
                xaxis_title_text='Fornight pay date', 
                yaxis_title_text='Total in AUD$',
                font_family='Arial',
                xaxis=dict(tickmode='array', tickvals= data2['Date'], ticktext = data2['Date'].apply(lambda x: x.strftime('%d-%b-%Y')),automargin=True)
                ),
            fig.update_yaxes(showgrid=False, range=[0,data1.max(numeric_only=True)], tickfont=dict(family='Arial', color='black', size=14),showline=True, linewidth=2, linecolor='black', mirror=False)
            fig.update_xaxes(type="category", tickfont=dict(family='Arial', color='black', size=14),showline=True, linewidth=2, linecolor='black', mirror=False)
            return html.Div(children=dcc.Graph(figure=fig), id='bar-chart')
        
        else:
            return html.Div("No data selected", className='no-data')

    return html.Div(id='bar-chart')
   
