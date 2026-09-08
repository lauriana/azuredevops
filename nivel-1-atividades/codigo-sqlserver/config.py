import os
import pyodbc
from dotenv import load_dotenv

# Esse arquivo, em específico, contém uma função para tentativa de conexão ao
# banco de dados em nuvem da Azure (Azure SQL Database), usando o driver ODBC.
# As credenciais do banco estão sendo lidas do .env, para não expor senha no código.
# Mais explicações se encontram no README.md desta pasta.

load_dotenv()


def connect_bd():
    try:
        connection_string = (
            "DRIVER={ODBC Driver 18 for SQL Server};"
            f"SERVER=tcp:{os.getenv('DB_HOST')},1433;"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')};"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )
        conn = pyodbc.connect(connection_string)
        print("Conectado ao banco com sucesso!")
        return conn
    except pyodbc.Error as e:
        print(f"Erro ao conectar: {e}")
        return None
