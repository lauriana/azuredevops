# Variante SQL Server do projeto loja

O projeto original (`project-devops-minicurso`, de renanolv7) só fala com **MySQL** — `src/main.py` e `src/database.py` usam `mysql-connector-python`. Esta pasta traz uma **variante equivalente**, escrita para o minicurso, que faz exatamente a mesma coisa (cadastrar e visualizar produtos) conectando a um **Azure SQL Database** via `pyodbc`.

> ⚠️ Este código não faz parte do repositório oficial do renanolv7 — é material de apoio deste minicurso, usado para adaptar o projeto original (que só fala MySQL) ao Azure SQL Database. Testado de ponta a ponta (estrutura de import e execução) contra o repositório real; revise antes de usar em produção.

> 💡 O projeto original organiza o código dentro de uma pasta `src/` (`src/main.py`, `src/database.py`) — não na raiz do projeto. Os dois arquivos desta pasta usam essa mesma estrutura para poderem simplesmente substituir os originais.

## Como usar

1. Termine o Setup Inicial (Passo 3: driver ODBC 18 instalado, Passo 4: Azure SQL Database criado)
2. Copie os dois arquivos desta pasta para dentro da pasta **`src/`** do seu projeto clonado, substituindo os originais:

```bash
cp codigo-sqlserver/database.py ../../project-devops-minicurso/src/database.py
cp codigo-sqlserver/main.py ../../project-devops-minicurso/src/main.py
```

(ajuste os caminhos conforme onde você clonou o projeto)

3. Copie `.env.example` também, para a **raiz** do projeto (não dentro de `src/`), e renomeie para `.env`:

```bash
cp codigo-sqlserver/.env.example ../../project-devops-minicurso/.env
```

4. Preencha o `.env` com os dados do seu Azure SQL Database (ver Parte 2, Atividade 4)
5. Instale a dependência que muda: `python -m pip install pyodbc python-dotenv` (em vez de `mysql-connector-python`)
6. Rode, **a partir da raiz do projeto** (não de dentro de `src/`):

```bash
python -m src.main
```

> ⚠️ Rodar `python main.py` ou `python src/main.py` diretamente **não funciona** — `main.py` importa com `from src.database import connect_bd`, um import que só resolve corretamente com `python -m src.main` executado da raiz do projeto.

## O que muda em relação ao original

| | MySQL (`mysql-connector-python`) | SQL Server (`pyodbc`) |
|---|---|---|
| Placeholder de parâmetro | `%s` | `?` |
| String de conexão | dicionário `host`/`user`/`password`/`database` | uma única string `DRIVER=...;SERVER=...;` |
| Coluna auto-incremento (na tabela) | `AUTO_INCREMENT` | `IDENTITY(1,1)` |
| Exceção de erro | `mysql.connector.Error` | `pyodbc.Error` |

A tabela `produtos` continua com as mesmas colunas (`nome_produto`, `valor`) — só a sintaxe do `CREATE TABLE` muda (ver Parte 2, Atividade 4).
