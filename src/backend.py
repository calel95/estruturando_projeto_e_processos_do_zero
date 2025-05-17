import pandas as pd
from schemas import Vendas, Categoria
import os

def process_excel(uploaded_file):
    try:
        # Read the Excel file
        df = pd.read_excel(uploaded_file)
        erros = []

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
        return  True, None
    
    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, f"Erro inesperado: {str(e)}"
    
def excel_to_sql(df):

