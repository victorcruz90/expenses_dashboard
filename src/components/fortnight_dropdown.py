from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from dash.exceptions import PreventUpdate

def render(app: Dash, data: pd) -> html.Div:

    data1 = data.groupby([pd.Grouper(key='Date', freq='2W-WED', closed='left', label='left')]).sum(numeric_only=True).reset_index()

    @app.callback(
        Output('fortnight-dropdown', 'value'),
        Input('select-all-button', 'n_clicks')
    )
    def update_dropdown(n_clicks):
        if n_clicks is None:
            raise PreventUpdate
        else:
            return data1['Date'].to_list()
    
    return html.Div(
        children=[
            html.H6('Date periods:', id='dropdown-header'),
            dcc.Dropdown(
                id='fortnight-dropdown',
                multi=True,
                options=[{'label': date_fortnight.date(), 'value': date_fortnight} for date_fortnight in data1['Date']],
                value=data1['Date'].iloc[-4:].to_list(),
                placeholder='Select fortnight initial date',
                style={
                    'width': "600px"}
            ),
            html.Br(),
            html.Button(
                className='button',
                children=['Select all'],
                id='select-all-button'
            )
        ]
    )