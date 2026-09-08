# Variante SQL Server do projeto loja

O projeto original (`project-devops-minicurso`, de renanolv7) só fala com **MySQL** — `main.py` e `config.py` usam `mysql-connector-python`. Esta pasta traz uma **variante equivalente**, escrita para o minicurso, que faz exatamente a mesma coisa (cadastrar e visualizar produtos) conectando a um **Azure SQL Database** via `pyodbc`.

> ⚠️ Este código não faz parte do repositório oficial do renanolv7 — é material de apoio deste minicurso para quem escolher a trilha SQL Server. Ele não foi testado contra um servidor Azure SQL real; revise antes de usar em produção.

## Como usar

1. Termine o Setup Inicial (Passo 3B: driver ODBC 18 instalado, Passo 4B: Azure SQL Database criado)
2. Copie os dois arquivos desta pasta para a **raiz** do seu projeto clonado, substituindo os originais:

```bash
cp codigo-sqlserver/config.py ../../project-devops-minicurso/config.py
cp codigo-sqlserver/main.py ../../project-devops-minicurso/main.py
```

(ajuste os caminhos conforme onde você clonou o projeto)

3. Copie `.env.example` também, para a raiz do projeto, e renomeie para `.env`:

```bash
cp codigo-sqlserver/.env.example ../../project-devops-minicurso/.env
```

4. Preencha o `.env` com os dados do seu Azure SQL Database (ver Parte 2, Atividade 4)
5. Instale a dependência que muda: `python -m pip install pyodbc python-dotenv` (em vez de `mysql-connector-python`)
6. Rode `python main.py` normalmente — o menu e o comportamento são idênticos à versão MySQL

## O que muda em relação ao original

| | MySQL (`mysql-connector-python`) | SQL Server (`pyodbc`) |
|---|---|---|
| Placeholder de parâmetro | `%s` | `?` |
| String de conexão | dicionário `host`/`user`/`password`/`database` | uma única string `DRIVER=...;SERVER=...;` |
| Coluna auto-incremento (na tabela) | `AUTO_INCREMENT` | `IDENTITY(1,1)` |
| Exceção de erro | `mysql.connector.Error` | `pyodbc.Error` |

A tabela `produtos` continua com as mesmas colunas (`nome_produto`, `valor`) — só a sintaxe do `CREATE TABLE` muda (ver Parte 2, Atividade 4B).
