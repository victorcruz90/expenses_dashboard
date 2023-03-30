import pandas as pd
import os

def load_bills_data(path : str) -> pd.DataFrame:
    data = pd.read_csv(path,header=0,dtype={"total_year": float})
    data["total_fortnight"] = data['total_year']/26
    data = data.round(2) 
        
    return data

def merge_data_from_files(path0: str, path1: str): 
    # List of file paths to be imported

    list_files_paths = [os.path.join(path0, filename) for filename in os.listdir(path0) if filename.endswith('.csv')]
    list_of_df = []

    #Import all the files
    for file_path in list_files_paths:
        df = pd.read_csv(file_path, 
                header=0,
                usecols=['Date', 'Amount', "Transaction Type", 'Transaction Details', 'Category', 'Merchant Name'],
                parse_dates=['Date'], 
            )
        # Filter the data from that dataFrame
        # Convert negative values into positive
        df['Amount'] = df['Amount'].abs()
        # Remove irrelevant transactions for the calculation
        df = df.query('Category != ["Transfers in","Bills", "Other income", "Transfers out", "Internal transfers", "Income"]').fillna('No detail')
        # Remove Morgage payment categorised as home
        df = df.query('Amount != 1100')

        list_of_df.append(df)

    df_final = pd.concat(list_of_df, ignore_index=True, axis=0).sort_values(by=['Date'], ascending=True).drop_duplicates()
    df_final.to_csv(path1, mode='a', index=False)   

def group_data(path: str):

    data = pd.read_csv(path, header=0,parse_dates=['Date'], dtype={'Amount': float})
    df_grouped = data.groupby([pd.Grouper(key='Date', freq='2W-WED', closed='left', label='left')]).sum(numeric_only=True).reset_index()
    data = data.groupby([pd.Grouper(key='Date', freq='2W-WED', closed='left', label='left'), "Category"]).sum(numeric_only=True).reset_index()
    return df_grouped, data

def expenses_date(path):
    data = pd.read_csv(path, header=0,parse_dates=['Date'], dtype={'Amount': float})
    
    return data

def current_fornight_balance(data_bills: pd, processed_data: pd, victor_balance, rebecca_balance, fort_amount):

    # Calculate the total each person pays in bills
    victor_bills = data_bills.query("person == 'Victor'")['total_year'].sum() / 26
    rebecca_bills = data_bills.query("person == 'Rebecca'")['total_year'].sum() / 26
    
    # Calculate money available after bills
    victor_money_after_bills = victor_balance - victor_bills
    rebecca_money_after_bills = rebecca_balance - rebecca_bills
    #Fornight Balance
    total_balance_fortnight = victor_money_after_bills + rebecca_money_after_bills - fort_amount
    number_fortnight = len(processed_data['Amount'])
    #Year Saving
    year_saving = number_fortnight*(victor_money_after_bills+rebecca_money_after_bills) - processed_data.Amount.sum()
    return total_balance_fortnight, year_saving
