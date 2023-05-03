from dash import Dash, html, dash_table
from dash.dash_table import FormatTemplate
from dash.dependencies import Output, Input, State
import pandas as pd
import dash


def render(app: Dash, data, path):
    @app.callback(
        Output('expenses', 'data'),
        Input('save-button', 'n_clicks'),
        Input('date-range-picker', 'start_date'),
        Input('date-range-picker', 'end_date'),
        State('expenses', 'data')
        )
    def update_data(n_clicks, start_date, end_date, rows):

        df = pd.DataFrame(rows)
        
        if dash.callback_context.triggered_id == 'save-button':
            # This callback is triggered by the save button, so update the data
            # df = pd.DataFrame(rows)
            df.to_csv(path, mode='w', index=False)

        elif start_date and end_date: 
            # This callback is triggered by the 'persistence' property, and there is saved data
            df = df.loc[(df['Date'] >= start_date) & (df['Date']<= end_date)]
        else:
            df = pd.read_csv(path)
        
        return df.to_dict('records')

    rows=data.to_dict('records')
    money = FormatTemplate.money(2)

    return html.Div(
        children=[
            dash_table.DataTable(id="expenses",
                data=rows,
                columns=[
                    dict(id="Date", name="Date"),
                    dict(id="Amount",name="Amount",type="numeric",format=money),
                    dict(id="Transaction Type", name="Transaction Type"),
                    dict(id="Transaction Details", name="Transation Details"),
                    dict(id='Category', name='Category', presentation='dropdown'),
                    dict(id='Merchant Name', name='Merchant Name')
                ],
                style_cell={"textAlign": "left"},
                fill_width=True,
                style_data={
                    "color": "black",
                    "font-family": "Arial, Helvetica, sans-serif",
                    "white-space": "normal",
                    'background-color': '#e6f7ff',
                    'border': '2px solid black'
                },
                style_header={
                    "color": "black",
                    "font-family": "Arial, Helvetica, sans-serif",
                    "font-weight": "bold",
                    'background-color': '#33bbff',
                    'border': '2px solid black'
                },
                style_table={
                    'border': '1px solid black'
                },
                
                editable=True,
                dropdown={
                    'Category': {
                        'options': [
                             {'label': i, 'value': i}
                                for i in data['Category'].unique()
                ]
            }},
                row_deletable=True,
                filter_action='native',
                filter_options={'case':'insensitive'},
                page_action='native',
                page_size=20,
                sort_action='native',
                persistence=True,
                persisted_props=['data'],
                persistence_type='local',
                )
        ],
        className="div-expenses-table",
    )
