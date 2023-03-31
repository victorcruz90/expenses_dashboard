from dash import Dash, html, dash_table
from dash.dash_table import FormatTemplate


def render(app: Dash, data):
    money = FormatTemplate.money(2)

    return html.Div(
        children=[
            dash_table.DataTable(
                data=data.to_dict("records"),
                id="bills",
                columns=[
                    dict(id="item", name="Item", type="numeric"),
                    dict(
                        id="total_year",
                        name="Total per year",
                        type="numeric",
                        format=money,
                    ),
                    dict(id="payment_type", name="Payment Type"),
                    dict(id="person", name="Person"),
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
                page_size=10
                
            )
        ],
        className="div-bills-table",
    )
