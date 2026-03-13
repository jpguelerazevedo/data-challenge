import pandas as pd
import warnings
from src.config import get_connection

warnings.filterwarnings('ignore', message='.*pandas only supports SQLAlchemy.*')

def retrieve_data(product_code=None, store_code=None, date=None):
    """
    Recupera um DataFrame da tabela data_product_sales aplicando filtros dinâmicos.
    A conexão é garantida internamente usando a função do nosso config.
    """
    conn = get_connection()
    if not conn or not conn.is_connected():
        print("Erro: Não foi possível conectar ao banco de dados.")
        return pd.DataFrame()
        
    query = "SELECT * FROM `looqbox-challenge`.data_product_sales WHERE 1=1"
    params = []
    
    if product_code is not None:
        query += " AND PRODUCT_CODE = %s"
        params.append(int(product_code))
        
    if store_code is not None:
        query += " AND STORE_CODE = %s"
        params.append(int(store_code))
        
    if date is not None and isinstance(date, list) and len(date) == 2:
        query += " AND DATE BETWEEN %s AND %s"
        params.extend(date)
        
    df = pd.read_sql(query, con=conn, params=tuple(params))
    conn.close()
    
    return df


if __name__ == "__main__":
    print("="*50)
    print(" FERRAMENTA DE BUSCA DATA_PRODUCT_SALES ")
    print("="*50)
    print("Deixe em branco e aperte ENTER se não quiser filtrar por um campo.\n")
    
    # Pegando o product_code do usuário
    p_code_input = input("Digite o product_code (inteiro): ").strip()
    p_code = int(p_code_input) if p_code_input.isdigit() else None
    
    # Pegando o store_code do usuário
    s_code_input = input("Digite o store_code (inteiro): ").strip()
    s_code = int(s_code_input) if s_code_input.isdigit() else None
    
    # Pegando o date do usuário
    date_start_input = input("Digite a data inicial [ex: 2019-01-01]: ").strip()
    date_end_input = input("Digite a data final [ex: 2019-01-31]: ").strip()
    
    date_list = None
    if date_start_input and date_end_input:
        date_list = [date_start_input, date_end_input]
    

    my_data = retrieve_data(product_code=p_code, store_code=s_code, date=date_list)
    
    print(f"\nResultado da busca (Total de linhas: {len(my_data)}):")
    if not my_data.empty:
        print(my_data)
    else:
        print("Nenhum dado encontrado com os filtros aplicados.")
