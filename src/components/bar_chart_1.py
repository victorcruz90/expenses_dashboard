from dash import Dash, html, dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd



def render(app: Dash, data: pd) -> html.Div:
    @app.callback(
        Output('bar-chart_1', 'children'),
        Input('expenses', 'data')
        )
    def update_graph(rows):

        #filtering the data
        data = pd.DataFrame(rows)
        data['Date'] = pd.to_datetime(data['Date'])
        
        data1 = data.query('Amount >= 0').reset_index()
        data2 = data.loc[data.Amount <= 0].copy()
        data2.Amount = data2.Amount.abs()
        df_expense = data2.groupby([pd.Grouper(key='Date', freq='2W-Wed', closed='left', label='left')]).sum(numeric_only=True).reset_index()
        df_income = data1.groupby([pd.Grouper(key='Date', freq='2W-Wed', closed='left', label='left')]).sum(numeric_only=True).reset_index()

        #Ploting the graph
        fig = go.Figure()

        fig.add_trace(go.Bar(x=df_income["Date"], y=df_income['Amount'],
        name = "Income", text = df_income["Amount"].round(2), textangle=0, textposition='outside', marker_color='#99ffeb'
        ))

        fig.add_trace(go.Bar(x=df_expense["Date"], y=df_expense['Amount'],
        name = "Expenses", text = df_expense["Amount"].round(2), textangle=0, textposition='outside', marker_color='#ff6666'
        ))

        
        # fig = px.bar(df_income, x='Date', y='Amount',color_discrete_sequence=px.colors.qualitative.Dark24, text_auto='.2f')
        # fig.layout(height=auto)
        fig.update_layout( 
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)', 
            bargap=0.1,
            xaxis_title_text='Fornight pay date', 
            yaxis_title_text='Total',
            font_family='Arial',
            xaxis=dict(tickmode='array', tickvals= df_expense['Date'], ticktext = df_expense['Date'].apply(lambda x: x.strftime('%d-%b-%Y')),automargin=True),
            )
        fig.update_yaxes(showgrid=False)
        
        return html.Div(children=dcc.Graph(figure=fig), id='bar-chart_1')
    


    return html.Div(id='bar-chart_1')