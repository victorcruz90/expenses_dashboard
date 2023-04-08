from dash import Dash, html, dash_table
from dash.dash_table import FormatTemplate
from dash.dependencies import Output, Input, State
import pandas as pd
import dash

# def get_data(path):
#     try:
#         df = pd.read_csv(path, he)
#     except pd.errors.EmptyDataError:
#         df = pd.DataFrame(columns=['Date', 'Amount', 'Transaction Type', 'Transaction Details', 'Category', 'Merchant Name'])
#     return df.to_dict('records')

def render(app: Dash, data, path):
    @app.callback(
        Output('expenses', 'data'),
        Input('save-button', 'n_clicks'),
        State('expenses', 'data'))
    def update_data(n_clicks, rows):
        if dash.callback_context.triggered[0]['prop_id'] == 'save-button.n_clicks':
            # This callback is triggered by the save button, so update the data
            df = pd.DataFrame(rows)
            df.to_csv(path, mode='w', index=False)
        # elif not persistence:
        #     # This callback is triggered by the 'persistence' property, and there is no saved data
        #     df = get_data(path)
        else:
            # This callback is triggered by the 'persistence' property, and there is saved data
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
                    dict(id='Category', name='Category'),
                    dict(id='Merchant Name', name='Merchant Name')
                ],
                style_cell={"textAlign": "left"},
                fill_width=True,
                style_data={
                    "color": "black",
                    "font-family": "Arial, Helvetica, sans-serif",
                    "white-space": "normal",
                    'background-color': 'rgb(191,239,181)',
                    'border': '2px solid black'
                },
                style_header={
                    "color": "black",
                    "font-family": "Arial, Helvetica, sans-serif",
                    "font-weight": "bold",
                    'background-color': 'rgb(91,168,91)',
                    'border': '2px solid black'
                },
                style_table={
                    'border': '1px solid black'
                },
                
                editable=True,
                row_deletable=True,
                filter_action='native',
                filter_options={'case':'insensitive'},
                page_action='native',
                page_size=20,
                sort_action='native',
                persistence=True,
                persisted_props=['data'],
                persistence_type='local'
                )
        ],
        className="div-expenses-table",
    )
