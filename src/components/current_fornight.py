from dash import Dash, html
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd



# def render(app: Dash, data: pd) -> html.Div:
#     @app.callback(
#         Output('bar-chart', 'children'),
#         [Input('save-button', 'n_clicks'), Input('expenses', 'data')]
#         )
#     def update_data(n_clicks, rows):

#         data = pd.DataFrame(rows, columns=['Date', 'Category', 'Amount'])
#         data['Date'] = pd.to_datetime(data['Date'])
#         data1 = data.groupby([pd.Grouper(key='Date', freq='2W-WED', closed='left', label='left'), "Category"]).sum(numeric_only=True).reset_index()
    


#     return html.Div(id='bar-chart')
   