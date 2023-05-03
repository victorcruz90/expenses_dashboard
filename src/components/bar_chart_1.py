from dash import Dash, html, dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd



def render(app: Dash, data: pd) -> html.Div:
    @app.callback(
        Output('bar-chart_1', 'children'),
        Input('expenses', 'data'),
        Input('fortnight-dropdown', 'value')
        )
    def update_graph(rows, fortnight_values: list):

        #filtering the data
        data = pd.DataFrame(rows)
        data['Date'] = pd.to_datetime(data['Date'])
        
        data1= data.query('Amount > 0')
        data2 = data.query('Amount < 0').copy()
        data2.Amount = data2.Amount.abs()
        df_expense = data2.groupby([pd.Grouper(key='Date', freq='2W-Wed', closed='left', label='left')]).sum(numeric_only=True).reset_index()
        df_income = data1.groupby([pd.Grouper(key='Date', freq='2W-Wed', closed='left', label='left')]).sum(numeric_only=True).reset_index()

        #Ploting the graph
        if fortnight_values:
            data_expense = df_expense.query('Date in @fortnight_values')
            data_income = df_income.query('Date in @fortnight_values')
            fig = go.Figure()
            
            fig.add_trace(go.Bar(x=data_income['Date'], y=data_income['Amount'],
            name = "Income", text = data_income['Amount'].round(2), textangle=0, textposition='outside', marker_color='#6fdc6f', marker_line=dict(width=2, color='black')
            ))

            fig.add_trace(go.Bar(x=data_expense["Date"], y=data_expense['Amount'],
            name = "Expenses", text = data_expense["Amount"].round(2), textangle=0, textposition='outside', marker_color='#ff6666', marker_line=dict(width=2, color='black')
            ))
            fig.update_layout( 
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', 
                bargap=0.05,
                xaxis_title_text='Fornight pay date', 
                yaxis_title_text='Total in AUD$',
                font_family='Arial',
                xaxis=dict(tickmode='array', tickvals= df_expense['Date'], ticktext = df_expense['Date'].apply(lambda x: x.strftime('%d-%b-%Y')),automargin=True),
                )
            fig.update_yaxes(showgrid=False, tickfont=dict(family='Arial', color='black', size=14),showline=True, linewidth=2, linecolor='black', mirror=False)
            fig.update_xaxes(type='category', tickfont=dict(family='Arial', color='black', size=14), showline=True, linewidth=2, linecolor='black', mirror=False)
            return html.Div(children=dcc.Graph(figure=fig), id='bar-chart_1')
        else:
            return html.Div("No data selected", className='no-data')


    return html.Div(id='bar-chart_1')