from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd


def render(app: Dash, data: pd) -> html.Div:
    return html.Div([dcc.DatePickerRange(
        id='date-range-picker',
        display_format='DD-MM-YYYY',
        min_date_allowed=data['Date'].min(),
        max_date_allowed=data['Date'].max(),
        initial_visible_month=data['Date'].max(),
        start_date_placeholder_text= 'Select date',
        end_date_placeholder_text='Select date',
              
    )
        ])