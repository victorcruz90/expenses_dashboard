from dash import Dash, html
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd
import dash



def render(app: Dash, data: pd) -> html.Div:
    @app.callback(
        Output('year-saving-text', 'children'),
        Input('expenses', 'data')
        )
    def update_data(rows):

        data = pd.DataFrame(rows, columns=['Date', 'Category', 'Amount'])
        data['Date'] = pd.to_datetime(data['Date'])
        data1 = data.groupby([pd.Grouper(key='Date', freq='2W-WED', closed='left', label='left')]).sum(numeric_only=True).reset_index()
    
        # Calculate the total each person pays in bills
        # victor_bills = bills.query("person == 'Victor'")['total_year'].sum() / 26
        # rebecca_bills = bills.query("person == 'Rebecca'")['total_year'].sum() / 26
    
        # Calculate money available after bills
        # victor_money_after_bills = 2566 - victor_bills
        # rebecca_money_after_bills = 1721 - rebecca_bills
        #Fornight Balance
        year_saving = data1['Amount'].sum()
        return html.I(children=f' AUD$ {year_saving:.2f}', className='fas fa-money-bill-wave' if year_saving >= 0 else 'fas fa-exclamation-triangle',
                style={'color': 'green' if year_saving >= 0 else 'red'})
     


    return html.Div([html.Div(id='year-saving-text')])
   