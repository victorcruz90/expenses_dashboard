from dash import Dash, html
import plotly.express as px
from src.components import bills_table, bar_chart, expenses_table
import dash_bootstrap_components as dbc
from src.data import loader

def create_layout(app : Dash, data_bills, bar_charts, data_expenses, path, fortnight_balance, year_saving) -> html.Div:

    # Table with bills
    card_one = dbc.Card([
        dbc.CardBody([
            html.P('List of Bills', id='bills-header'),
            bills_table.render(app, data_bills)
        ],
        style={'height': 'auto',
               'witdh': 'auto'
               }
        )],
        id='card-one')

    # Fortnight balance 
    card_two = dbc.Card([
        dbc.CardBody([
            html.P('Current Fornight Balance', id='current-balance-header'),
            html.P(
                [html.I(f' AUD {fortnight_balance:.2f}',
                className='fas fa-money-bill-wave' if fortnight_balance >= 0 else 'fas fa-exclamation-triangle',
                style={'color': 'green' if fortnight_balance >= 0 else 'red'})], 
                id='balance-text'
                )
        ],
        style={'height': 'auto',
                'witdh': 'auto',
               })
    ], 
        id='card-two')
    
    #  Saved in the year
    card_three = dbc.Card([
        dbc.CardBody([
            html.P('Amount Saved in 2023', id='save-amount-header'),
            html.P(
                [html.I(f' AUD {year_saving:.2f}',
                className='fas fa-money-bill-wave' if year_saving >= 0 else 'fas fa-exclamation-triangle',
                style={'color': 'green' if year_saving >= 0 else 'red'})], 
                id='year-text'
                )
            ],
            style={'height': 'auto',
               'witdh': 'auto'})
        ], 
        id='card-three')
    
    #  bar chart 
    card_four = dbc.Card(
        dbc.CardBody([
            html.P('Fortnight Expenditure', id='bar-chart-header'),
            html.Div(bar_chart.render(app, bar_charts), id='bar-chart')],
            style={'height': 'auto',
               'witdh': 'auto'}, 
        ), 
        id='card-four'
    )

    card_five = dbc.Card([
        dbc.CardBody([
            html.P('List of Expenses', id='expenses-header'),
            html.Button('Save', id ='save-button'),
            expenses_table.render(app, data_expenses, path)
        ],
        style={'height': 'auto',
               'witdh': 'auto'
               }
        )],
        id='card-five')

    app_layout = html.Div([
        html.Link(rel='stylesheet', href='https://use.fontawesome.com/releases/v5.0.13/css/all.css'),
        dbc.Row([
            dbc.Col([card_two]),
            dbc.Col([card_three])
            ]),
        html.Br(),
        dbc.Row([
            dbc.Col([card_four])
            ]),
        html.Br(),
        dbc.Row([card_five]),
        html.Br(),
        dbc.Row([card_one])
        ], className='main-div'
    )

    return app_layout