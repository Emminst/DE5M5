import pandas as pd
df = pd.read_csv('Python/Data/03_Library Systembook.csv')
df.fillna('n/a')
df_clean = df.dropna()
df_clean.loc[df_clean['Book checkout'].notna(), 'Book checkout'] = df_clean['Book checkout'].str.replace('"', '')

data_enriched = df_clean

data_enriched['loan_duration'] = (data_enriched['Book Returned'] - data_enriched['Book checkout']).dt.days
valid_loan_data = data_enriched[data_enriched['loan_duration']>=0]

from sqlalchemy import create_engine
server = 'localhost'
database = 'DE5M5'
driver = 'ODBC Driver 17 for SQL Server'
connection_string = f'mssql+pyodbc://@{server}/{database}?driver={driver}'
engine = create_engine(connection_string)

df = pd.DataFrame(df_valid_loan_data)
df.to_sql('Books', engine, if_exists='replace', index=False)