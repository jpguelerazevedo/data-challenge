# Looqbox Data Challenge - Soluções

Bem-vindo ao repositório com as soluções do Looqbox Data Challenge! Este projeto foi estruturado de forma modular e conta com scripts em Python integrados a um banco de dados MySQL para resolver os três cases de negócio.

## 📌 Requisitos do Sistema
Para executar este projeto, certifique-se de que possui instalado em sua máquina:
- Python 3.8+
- [Git](https://git-scm.com/) (opcional, para clonar)

## ⚙️ Configuração Inicial

### 1. Criar e Ativar Ambiente Virtual (Recomendado)
Para isolar as dependências deste projeto das da sua máquina, crie um ambiente virtual na raiz do projeto:

**No Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**No Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instalar as Dependências
Com o ambiente ativado, instale as bibliotecas necessárias listadas no `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Configurar as Variáveis de Ambiente
O projeto precisa das credenciais do banco de dados para rodar. Utilize de base o `.env.exemple` e crie um arquivo chamado `.env` na raiz do projeto contendo as variáveis abaixo:

```env
DB_HOST= #IP do banco de dados
DB_PORT= #Porta do banco de dados
DB_USER= #Usuário do banco de dados
DB_PASS= #Senha do banco de dados
DB_NAME= #Nome do banco de dados
```

---

### 📝 Respostas do Teste de SQL (Base)
As queries referentes às 3 primeiras perguntas de "SQL test" estão disponíveis dentro da pasta `tests/` na raiz do projeto (`testSQL_1.txt`, `testSQL_2.txt` e `testSQL_3.txt`).
> **Aviso Importante:** Para utilizar e testar essas queries, é rigorosamente necessário possuir uma ferramenta/cliente de SGBD (como DBeaver, MySQL Workbench, VS Code Database Client, ou Terminal do MySQL) e **estar previamente conectado ao servidor remoto** utilizando exatamente as credenciais de banco de dados fornecidas pelo recrutador no e-mail do desafio. Selecione o schema `looqbox_challenge` antes de executar as consultas.

## 🚀 Como Executar os Cases

Os scripts foram desenvolvidos como módulos na pasta `src/`. Certifique-se sempre de estar na raiz do projeto e com o ambiente virtual ativado na hora de rodar os comandos no terminal.

### Case 1: Função de Consulta Dinâmica
Este script implementa uma função flexível (`retrieve_data`) capaz de cruzar dados da tabela `data_product_sales`. Ele roda com uma interface interativa no terminal para que o usuário informe os parâmetros.
* **Comando:**
  ```bash
  python3 -m src.cases.case1
  ```
* **O que esperar:** O terminal fará perguntas sobre os IDs de produtos, lojas e intervalo de datas. Deixe em branco se quiser não filtrar por aquele atributo e receba o dataframe resultante na tela.

### Case 2: Filtragem via Pandas com Tabela Markdown
Aqui pegamos consultas estáticas, rodamos via Pandas e simulamos um filtro na tabela com o período determinado, finalizando com a criação de uma métrica extra (Ticket Médio/TM) e a renderização em formato Visual de Markdown.
* **Comando:**
  ```bash
  python3 -m src.cases.case2
  ```
* **O que esperar:** O processamento interno via Pandas ocorrerá e uma tabela lindamente formatada será printada diretamente no seu terminal correspondendo exatamente à imagem alvo requerida.

### Case 3: Visualização/Gráfico do IMDb
Script focado em Data Visualization utilizando Seaborn e Matplotlib. Acessa as informações de filmes para demonstrar a distribuição global de notas no sistema através de um Histograma de Curva de Densidade.
* **Comando:**
  ```bash
  python3 -m src.cases.case3
  ```
* **O que esperar:** O script não abrirá janelas interativas. Em vez disso, criará uma pasta chamada `outputs_case3/` automaticamente na raiz do projeto e salvará uma imagem de alta qualidade (PNG, 300dpi) nela com o resultado da sua análise.

---