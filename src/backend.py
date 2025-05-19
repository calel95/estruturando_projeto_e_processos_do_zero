import pandas as pd
from schemas import Vendas, Categoria
import os
from dotenv import load_dotenv


load_dotenv(".env")

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

def process_excel(uploaded_file):
    try:
        # Read the Excel file
        df = pd.read_excel(uploaded_file)

        #Validate if exists extra columns
        extra_columns = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_columns:
            return False, f"Colunas extras detectadas no arquivo: {', '.join(extra_columns)}"
        
        # Validate each sheet
        for index, row in df.iterrows():
            try:
                # Validate the row data
                _ = Vendas(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Erro na linha {index + 2}: {e}")
        return  df, True, None
    
    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Erro inesperado: {str(e)}"
    
def excel_to_sql(df):
    df.to_sql(
        name='vendas',
        con=POSTGRES_URL,
        if_exists='replace',
        index=False
    )
