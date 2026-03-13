import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
from src.config import get_connection

warnings.filterwarnings('ignore', message='.*pandas only supports SQLAlchemy.*')

def run_case3():
    # Obtem conexão com o banco de dados
    conn = get_connection()
    if not conn:
        print("Erro ao conectar no banco de dados.")
        return

    try:
        print("Extraindo os dados da tabela IMDB_movies...")
        query = "SELECT * FROM IMDB_movies"
        df = pd.read_sql(query, con=conn)
    finally:
        conn.close()

    if df.empty:
        print("A tabela IMDB_movies está vazia ou não foi encontrada.")
        return

    rating_col = 'Rating'

    print(f"Gerando o gráfico de histograma baseado na coluna: {rating_col}...")

    # Gerando o Gráfico (Histograma de Distribuição)
    plt.figure(figsize=(10, 6))
    
    # x=rating_col (Eixo X): Representa as notas da coluna 'Rating'
    # O Eixo Y será gerado automaticamente pelo histplot e representará
    # a quantidade de filmes incluídos em cada faixa de nota
    sns.histplot(data=df, x=rating_col, bins=20, kde=True, color='#6C63FF', alpha=0.7)
    
    plt.title(f'Distribuição de Notas dos Filmes (IMDB)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Nota do Filme (Rating)', fontsize=12)
    plt.ylabel('Quantidade de Filmes', fontsize=12)
    
    # Adiciona a linha com a média global de todas as notas
    mean_val = df[rating_col].mean()
    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Nota Média: {mean_val:.2f}')
    plt.legend()
    
    sns.despine() # Remove as bordas do topo e lado direito
    
    plt.tight_layout()
    
    # Cria pasta para salvar as saídas, se não existir
    output_dir = "outputs_case3"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Salva o gráfico como imagem
    file_path = os.path.join(output_dir, "visualizacao_case3.png")
    
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    print(f"Gráfico gerado com sucesso! Salvo em: {file_path}")

if __name__ == "__main__":
    run_case3()