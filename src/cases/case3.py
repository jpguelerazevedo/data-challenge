import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_imdb_visualization(connection):
    """
    Gera uma visualização da tabela IMDB_movies.
    
    Parâmetros:
    - connection: objeto de conexão com o banco de dados
    """
    # 1. Puxando os dados do banco
    query = "SELECT * FROM looqbox_challenge.IMDB_movies"
    df = pd.read_sql(query, con=connection)
    
    # Imprime as colunas no terminal para conferência
    print("\nColunas encontradas na tabela IMDB_movies:")
    print(df.columns.tolist())
    
    # 2. Identificando a coluna de classificação (Rating) de forma dinâmica
    # Procuramos por variações da palavra rating ou score na tabela
    rating_col = None
    for col in df.columns:
        if 'rating' in col.lower() or 'score' in col.lower():
            rating_col = col
            break
            
    # Se não achar pelo nome, usa a última coluna numérica por segurança
    if not rating_col:
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        rating_col = numeric_cols[-1] if len(numeric_cols) > 0 else df.columns[1]

    # 3. Gerando o Gráfico (Histograma de Distribuição de Notas)
    plt.figure(figsize=(10, 6))
    
    # Criamos um histograma com linha de densidade para ver o formato da distribuição
    sns.histplot(data=df, x=rating_col, bins=20, kde=True, color='#6C63FF', alpha=0.7)
    
    plt.title(f'Distribuição das Notas dos Filmes ({rating_col})', fontsize=16, fontweight='bold')
    plt.xlabel('Nota (Rating)', fontsize=12)
    plt.ylabel('Quantidade de Filmes', fontsize=12)
    
    # Adicionando uma linha de média para enriquecer o gráfico
    mean_rating = df[rating_col].mean()
    plt.axvline(mean_rating, color='red', linestyle='dashed', linewidth=2, label=f'Média: {mean_rating:.2f}')
    plt.legend()
    
    # Remove as bordas superior e direita para deixar o gráfico mais limpo (boa prática de DataViz)
    sns.despine()
    
    plt.tight_layout()
    plt.show()

EXPLANATION = """
📝 JUSTIFICATIVA DA ESCOLHA DO GRÁFICO:

Escolhi um Histograma com Linha de Densidade (KDE) focado na distribuição das notas (Ratings) dos filmes.

Por que essa visualização?
1. É frequentemente o primeiro passo em Análise Exploratória de Dados (EDA) para entender o "comportamento geral" do dataset.
2. Ajuda a responder visualmente de forma rápida: 
   - "A maioria dos filmes dessa base são bons ou ruins?"
   - "As notas seguem uma distribuição normal (curva de sino) ou há um desvio para notas muito altas/baixas?"
3. A adição da linha vermelha vertical apontando a média facilita muito a leitura por pessoas de negócios, que batem o olho e já sabem qual é o padrão de nota do catálogo.
"""

if __name__ == "__main__":
    # Exemplo de chamada:
    # conn = mysql.connector.connect(...)
    # generate_imdb_visualization(connection=conn)
    
    print(EXPLANATION)
