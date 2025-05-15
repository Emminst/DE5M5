import pandas as pd
from sqlalchemy import create_engine
#import pyodbc

# Function to output dataframe that can be manipulated via a filepath
def fileLoader(filepath):
    data = pd.read_csv(filepath)
    return data 

# Duplicate Dropping Function
def duplicateCleaner(df):
    return df.drop_duplicates().reset_index(drop=True)

# NA handler - future scope can handle errors more elegantly. 
def naCleaner(df):
    return df.dropna().reset_index(drop=True)

# Turning date columns into datetime
def dateCleaner(col, df):
    #date_errors = pd.DataFrame(columns=df.columns)  # Store rows with date errors

    # Strip any quotes from dates
    df[col] = df[col].str.replace('"', "", regex=True)

    try:
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')

    except Exception as e:
        print(f"Error while converting column {col} to datetime: {e}")

    # Identify rows with invalid dates
    error_flag = pd.to_datetime(df[col], dayfirst=True, errors='coerce').isna()
        
    # Move invalid rows to date_errors - Future feature
    #date_errors = df[error_flag]
        
    # Keep only valid rows in df
    df = df[~error_flag].copy()

    # Reset index for the cleaned DataFrame
    df.reset_index(drop=True, inplace=True)

    return df

def enrich_dateDuration(colA, colB, df):
    """
    Takes the two datetime input column names and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
    
    Note:
      colB>colA
    """
    df['date_delta'] = (df[colB]-df[colA]).dt.days

    #Conditional Filtering to be able to gauge eroneous loans.
    df.loc[df['date_delta'] < 0, 'valid_loan_flag'] = False
    df.loc[df['date_delta'] >= 0, 'valid_loan_flag'] = True

    return df

def writeToSQL(df, table_name, server, database):

    # Create the connection string with Windows Authentication
    connection_string = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'

    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)

    try:
        # Write the DataFrame to SQL Server
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        print(f"Table{table_name} written to SQL")
    except Exception as e:
        print(f"Error writing to the SQL Server: {e}")

if __name__ == '__main__':
    print('**************** Starting Clean ****************')

    # Instantiation
    #dropCount= 0
    #customer_drop_count = 0
    filepath_input = 'Python/Data/03_Library Systembook.csv'
    date_columns = ['Book checkout', 'Book Returned']
    date_errors = None

    data = fileLoader(filepath=filepath_input)

    # Initialize invalid dates error counter
    error_count = 0  

    # Converting the date of purchase to date format
    try: 
        data['Book checkout'] = data['Book checkout'].str.replace('"', "", regex=True)
        data['Book checkout'] = pd.to_datetime(data['Book checkout'], format='mixed' ) 
        data.head()
    except Exception as e:
        error_count += 1  # Increment error counter
        print(f'Error count: {error_count}, Error Occured: {e}')

    #count data before dropping duplicates
    initial_rows = len(data)

    # Drop duplicates & NAs
    data = duplicateCleaner(data)
    data = naCleaner(data)

    #count data after dropping duplicates
    final_rows = len(data)

    # Calculate number dropped rows
    dropped_row_count = initial_rows - final_rows
    print(f'Number of rows dropped: {dropped_row_count}')

    # Converting date columns into datetime
    for col in date_columns:
        data = dateCleaner(col, data)
  
    # Enriching the dataset
    data = enrich_dateDuration(df=data, colA='Book Returned', colB='Book checkout')

    # Calculate duration
    data['Duration'] = (data['Book Returned'] - data['Book checkout']).dt.days
    
    # Identify negative durations
    negative_rows = data[data['Duration'] < 0]

    # Count negative entries
    negative_count = len(negative_rows)

    print(f'Total negative durations: {negative_count}')

    #data.to_csv('cleaned_file.csv')
    print(data)

    #Cleaning the customer file
    filepath_input_2 = 'Python/Data/03_Library SystemCustomers.csv'

    data2 = fileLoader(filepath=filepath_input_2)

    # Drop duplicates & NAs
    data2 = duplicateCleaner(data2)
    data2 = naCleaner(data2)

    print(data2)
    print('**************** DATA CLEANED ****************')


    # print('Writing to SQL Server...')

    # writeToSQL(
    #     data, 
    #     table_name='loans_bronze', 
    #     server = 'localhost', 
    #     database = 'DE5_Module5' 
    # )

    # writeToSQL(
    #     data2, 
    #     table_name='customer_bronze', 
    #     server = 'localhost', 
    #     database = 'DE5_Module5'
    # )
    # print('**************** End ****************')
    