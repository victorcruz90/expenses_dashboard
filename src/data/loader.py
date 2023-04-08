import pandas as pd
import os

def load_bills_data(path : str) -> pd.DataFrame:
    data = pd.read_csv(path,header=0,dtype={"total_year": float})
    data["total_fortnight"] = data['total_year']/26
    data = data.round(2) 
        
    return data

def merge_data_from_files(path0: str, path1: str, path2: str): 
    # List of file paths to be imported

    list_files_paths = [os.path.join(path0, filename) for filename in os.listdir(path0) if filename.endswith('.csv')]
    list_of_df = []

    #Import all the files and 
    if len(os.listdir(path0)) > 1:
        for file_path in list_files_paths:
            df = pd.read_csv(file_path, 
                    header=0,
                    usecols=['Date', 'Amount', "Transaction Type", 'Transaction Details', 'Category', 'Merchant Name'],
                    parse_dates=['Date']
                )
            # Filter the data from that dataFrame
            # Convert negative values into positive
            # df['Amount'] = df['Amount'].abs()
            # Remove irrelevant transactions for the calculation
            df = df.query('Category != ["Internal transfers"]').fillna('No detail')
            # Remove Morgage payment categorised as home
            # df = df.query('Amount != 1100')

            list_of_df.append(df)
            if file_path.endswith('.csv'):
                os.remove(file_path)

        # Save data into path1
        df_final = pd.concat(list_of_df, ignore_index=True, axis=0).sort_values(by=['Date'], ascending=True).drop_duplicates()
        df_final.to_csv(path1, mode='a', index=False, header=False)
        df_final.to_csv(path2, mode='a', index=False, header=False)

    #Load the expenses data after merging and cleaning to return as Dataframe from path1
    df_all = pd.read_csv(path1, header=0,
                parse_dates=['Date']) 


    return df_all
    

