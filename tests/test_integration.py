import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine



load_dotenv(".env")

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


#POSTGRES_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#POSTGRES_URL = "postgresql+psycopg2://dbname_pmm7_user:M0XEO8YJXzrFD7M7Wiqq3beTF9Keh2iJ@dpg-d0j9lb63jp1c739mfnfg-a.oregon-postgres.render.com:5432/dbname_pmm7"
#engine = create_engine(POSTGRES_URL)


def test_postgres_connection_and_schema():
    df = pd.read_sql('SELECT * FROM vendas',con=POSTGRES_URL)
    #df = pd.read_sql('SELECT * FROM vendas', con=engine)


    assert not df.empty, "DataFrame is empty, assure that the your connection or query is right"

    expected_dtype = {
        'email': 'object',  # object em Pandas corresponde a string em SQL
        'data': 'datetime64[ns]',
        'valor': 'float64',
        'quantidade': 'int64',
        'produto': 'object',
        'categoria': 'object'
    }

    assert df.dtypes.to_dict() == expected_dtype, "DataFrame schema does not match expected schema"
