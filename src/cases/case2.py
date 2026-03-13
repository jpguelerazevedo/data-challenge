import pandas as pd
import warnings
from src.config import get_connection

warnings.filterwarnings('ignore', message='.*pandas only supports SQLAlchemy.*')

def run_case2():
    # 1. Queries
    query_cad = """
    SELECT
          STORE_CODE,
          STORE_NAME,
          START_DATE,
          END_DATE,
          BUSINESS_NAME,
          BUSINESS_CODE
    FROM data_store_cad
    """

    query_sales = """
    SELECT
            STORE_CODE,
            DATE,
            SALES_VALUE,
            SALES_QTY
    FROM data_store_sales
    WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31'
    """

    # Conexão com o banco de dados
    conn = get_connection()
    if not conn:
        print("Erro ao conectar no banco de dados.")
        return

    try:
        # Extrai os dados utilizando as queries fornecidas
        print("Extraindo os dados do banco...")
        df_cad = pd.read_sql(query_cad, conn)
        df_sales = pd.read_sql(query_sales, conn)
    finally:
        conn.close()

    # 2. Filtra o período ['2019-10-01','2019-12-31'] em Python (Pandas)
    df_sales['DATE'] = pd.to_datetime(df_sales['DATE'])
    mask = (df_sales['DATE'] >= '2019-10-01') & (df_sales['DATE'] <= '2019-12-31')
    df_sales_filtered = df_sales[mask]

    # Junta os dataframes usando a ligação STORE_CODE para ter nomes das lojas e negócios
    df_merged = pd.merge(df_sales_filtered, df_cad, on='STORE_CODE', how='inner')

    # 3. Constrói a visualização requerida
    # Agrupa por Loja (STORE_NAME) e Categoria (BUSINESS_NAME)
    df_grouped = df_merged.groupby(['STORE_NAME', 'BUSINESS_NAME']).agg(
        TOTAL_VALUE=('SALES_VALUE', 'sum'),
        TOTAL_QTY=('SALES_QTY', 'sum')
    ).reset_index()

    # Calcula o TM (Ticket Médio = Valor Total / Quantidade Total)
    df_grouped['TM'] = df_grouped['TOTAL_VALUE'] / df_grouped['TOTAL_QTY']

    # Monta o dataframe final 
    df_final = pd.DataFrame({
        'Loja': df_grouped['STORE_NAME'],
        'Categoria': df_grouped['BUSINESS_NAME'],
        'TM': df_grouped['TM'].round(2) # Arredondando para 2 núneros decimais
    })

    # Ordenar pelos Nomes das Lojas
    df_final = df_final.sort_values(by='Loja').reset_index(drop=True)

    # Imprimir o DataFrame em formato Markdown para uma bela visualização no terminal
    print("\nVisualização Solicitada (Case 2):\n")
    print(df_final.to_string(index=False))


if __name__ == "__main__":
    run_case2()