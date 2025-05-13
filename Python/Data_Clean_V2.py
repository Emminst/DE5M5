import pandas as pd

df = pd.read_csv('Python/Data/03_Library Systembook.csv')
df_clean = df.dropna()

"""
df_clean.drop(16, axis=0, inplace=True)

df_clean['Book checkout'] = pd.to_datetime(df_clean['Book checkout'],format, dayfirst=True)
df_clean['Book Returned'] = pd.to_datetime(df_clean['Book Returned'],format, dayfirst=True)

data_enriched = df_clean.copy()
data_enriched['loan_duration'] = (data_enriched['Book Returned'] - data_enriched['Book checkout']).dt.days
valid_loan_data = data_enriched[data_enriched['loan_duration']>=0]
"""

from sqlalchemy import create_engine
server = 'localhost'
database = 'DE5M5'
driver = 'ODBC Driver 17 for SQL Server'
connection_string = f'mssql+pyodbc://@{server}/{database}?driver={driver}'
engine = create_engine(connection_string)

#df = pd.DataFrame(valid_loan_data)
df = pd.DataFrame(df_clean)

df.to_sql('Books', engine, if_exists='replace', index=False)

df.to_csv('Python/Data/cleaned_dataset.csv',index=False)