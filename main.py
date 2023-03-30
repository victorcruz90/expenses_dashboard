from dash import Dash, html, dcc, dash_table
from src.components.layout import create_layout
import dash_bootstrap_components as dbc 
from src.data.loader import *
import pandas as pd
import os




def main():
    # Variables
    BILLS_FILE_PATH = './data/processed/Bills.csv'

    FOLDER_PROCESSED = './data/processed/'

    FOLDER_RAW = './data/raw/'

    ALL_DATA = 'expenses_filtered_2023.csv'
    # Load bills table data
    bills_data = load_bills_data(BILLS_FILE_PATH)

     # This section will try to run
    if len(os.listdir(FOLDER_RAW)) > 1:
        # Merge and save filtered data
        merge_data_from_files(FOLDER_RAW, os.path.join(FOLDER_PROCESSED, ALL_DATA))
        # Delete files 
        for file in os.listdir(FOLDER_RAW):
            if file.endswith('.csv'):
                os.remove(os.path.join(FOLDER_RAW, file))

    # Load and Group Data
    data_expense = expenses_date(os.path.join(FOLDER_PROCESSED, ALL_DATA))
    processed_fort_data, processed_cat_data  = group_data(os.path.join(FOLDER_PROCESSED, ALL_DATA))
    

    # Current Fornight balance and Amount saved in 2023
    victor_balance = 2566
    rebecca_balance = 1721
    fort_amount = processed_fort_data.iloc[-1]['Amount']
    fort_balance, year_saving = current_fornight_balance(bills_data, processed_data=processed_fort_data, victor_balance=victor_balance, rebecca_balance=rebecca_balance, fort_amount=fort_amount)


    # Section to run the app
    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])
    app.title = "Expenses Dashboard"
    app.layout= create_layout(app, bills_data, processed_cat_data, data_expense, os.path.join(FOLDER_PROCESSED,ALL_DATA), fort_balance, year_saving)
    app.run(debug=True)


if __name__ == "__main__":
    main()