from dash import Dash, html, dcc
import pandas as pd


def render(app: Dash, data: pd) -> html.Div:

    data1 = data.groupby([pd.Grouper(key='Date', freq='2W-WED', closed='left', label='left')]).sum(numeric_only=True).reset_index()

    return html.Div(
        children=[
            html.H6('Date periods:'),
            dcc.Dropdown(
                id='fortnight-dropdown',
                multi=True,
                options=[{'label': date_fortnight.date(), 'value': date_fortnight} for date_fortnight in data1['Date']],
                value=None
            ),
            html.Br(),
            html.Button(
                className='button',
                children=['Select all'],
                id='select-all-button'
            )
        ]
    )