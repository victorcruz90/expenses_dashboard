from dash import Dash, html
import plotly.express as px
from src.components import current_fornight, bar_chart, expenses_table, year_saving, bar_chart_1, fortnight_dropdown, datarangepicker
import dash_bootstrap_components as dbc
from src.data import loader

def create_layout(app : Dash, data_expenses, path) -> html.Div:

    # Table with bills
    card_one = dbc.Card(
        dbc.CardBody([
        html.P('Expenses against Income', id='expense-vs-income-header'),
        bar_chart_1.render(app, data_expenses)]),
        style={'height': 'auto',
               'witdh': 'auto'}, 
        id='card-one')

    # Fortnight balance 
    card_two = dbc.Card([
        dbc.CardBody([
            html.P('Last Fornight Balance', id='current-balance-header'),
            html.P(current_fornight.render(app, data_expenses))
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
            html.P(year_saving.render(app, data_expenses))
            ],
            style={'height': 'auto',
               'witdh': 'auto'})
        ], 
        id='card-three')
    
    #  bar chart 
    card_four = dbc.Card(
        dbc.CardBody([
            html.P('Fortnight Expenditure per Category', id='bar-chart-header'),
            html.Br(),
            fortnight_dropdown.render(app, data_expenses),
            bar_chart.render(app, data_expenses),
            # html.Br(),
            # html.P('Expenses against Income', id='expense-vs-income-header'),
            # bar_chart_1.render(app, data_expenses)
            ]),
            style={'height': 'auto',
               'witdh': 'auto'}, 
        id='card-four')
    
    
    card_five = dbc.Card([
        dbc.CardBody([
            html.P('List of Expenses', id='expenses-header'),
            html.Button('Save', id='save-button', className='button'),
            html.Br(),
            html.Br(),
            datarangepicker.render(app, data_expenses),
            html.Br(),
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
        dbc.Row([
            dbc.Col([card_one])
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col([card_five])
        ]),
        ], className='main-div'
    )

    return app_layout