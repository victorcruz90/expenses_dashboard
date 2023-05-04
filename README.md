# Code Description

This code is a Python script that runs a web application using Dash framework. It loads and processes financial data to display it in a dashboard format. The script consists of several functions that load and process data from CSV files located in specific paths. It also defines a layout for the web app using the create_layout function from src.components.layout module. Finally, it creates a Dash app instance and runs it using the layout and data processed.


# Installation and Usage

To run this code, you need to do the following:



Install Python 3.7 or higher

Clone the repository where this code resides in.

Install the required Python packages using the command pip install -r requirements.txt.

Ensure that the financial data CSV files are saved in the specified paths in the script.

Run the script using the command python main.py.

Access the web app via localhost in a browser session.


# Note on the Financial Data

The financial data that this script uses must follow a specific structure for proper processing, and the CSV files must be saved in specific paths. These requirements are specified in the script. It is important to ensure that the financial data CSV files match these requirements, or this code may not run correctly.

# Issues

1. Bar chart does not keep the updated value after datable edit and page reload. (Solved)

2. Current_fornight_balance and year_savings are not updating with the change in datatable.(Solved)

3. DataTable is not connect to date range picker. Cannot filter data by date range. (Solved)

4. When selecting dropwdown dates, the updated graph has random gaps between the bins (Solved).

5. Data range picker filter bar charts and overides the dropdown filtering (Solved). 


# Current Developments

1. add Dropdown to bar charts (DONE)

2. Aggregate both bar charts to the same card in the dashboard.

