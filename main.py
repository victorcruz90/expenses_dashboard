from dash import Dash, html, dcc, dash_table
from src.components.layout import create_layout
import dash_bootstrap_components as dbc 
from src.data.loader import *
import pandas as pd
import os




def main():
    # Variables
    # BILLS_FILE_PATH = './data/processed/Bills.csv'

    FOLDER_PROCESSED = './data/processed/'

    FOLDER_RAW = './data/raw/'

    ALL_DATA = 'expenses_filtered_2023.csv'

    ALL_DATA_ORIGINAL = 'expenses_filtered_2023_original.csv'
                
    # Merge data and check whether it has new files
    data_expense = merge_data_from_files(FOLDER_RAW, os.path.join(FOLDER_PROCESSED, ALL_DATA), os.path.join(FOLDER_PROCESSED, ALL_DATA_ORIGINAL))
    
    # Load bills data
    # bills_data = load_bills_data(BILLS_FILE_PATH)

    # Section to run the app
    app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])
    app.title = "Expenses Dashboard"
    app.layout= create_layout(app, data_expense, os.path.join(FOLDER_PROCESSED,ALL_DATA))
    app.run(debug=True)


if __name__ == "__main__":
    main()