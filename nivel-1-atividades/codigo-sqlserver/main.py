import sys

from src.database import connect_bd

# Conecta ao banco de dados uma única vez, quando o programa inicia
conexao = connect_bd()

if conexao is None:
    # connect_bd() já imprimiu o motivo do erro (driver, rede, credenciais).
    # Sem isso aqui, o programa travaria mais na frente com um
    # "AttributeError: 'NoneType' object has no attribute 'cursor'" bem
    # mais confuso do que a mensagem que connect_bd() já mostrou.
    print("Não foi possível conectar ao banco de dados. Revise o .env, o driver ODBC 18 e a rede (porta 1433 liberada) antes de tentar de novo.")
    sys.exit(1)


def cadastrar_produto():
    # Pergunta o nome e o valor, e salva um novo produto no banco
    cursor = conexao.cursor()

    nome_produto = input("Nome do produto: ")
    valor = float(input("Valor do produto: "))

    # O pyodbc usa "?" como placeholder (o mysql-connector usa "%s") — o driver
    # preenche esse espaço de forma segura, sem risco de SQL Injection.
    query = "INSERT INTO produtos (nome_produto, valor) VALUES (?, ?)"
    cursor.execute(query, (nome_produto, valor))
    conexao.commit()

    cursor.close()
    print("Produto cadastrado com sucesso!\n")


def visualizar_produtos():

    cursor = conexao.cursor()

    cursor.execute("SELECT nome_produto, valor FROM produtos")
    produtos = cursor.fetchall()

    cursor.close()

    if not produtos:
        print("Nenhum produto cadastrado ainda.\n")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")
    for nome_produto, valor in produtos:
        print(f"{nome_produto} - R$ {valor:.2f}")
    print()


def exibir_menu():
    print("===========================================")
    print("=      (1) - Cadastrar produto            =")
    print("=      (2) - Visualizar produtos          =")
    print("=      (3) - Sair                         =")
    print("===========================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            visualizar_produtos()
        elif opcao == "3":
            print("\nAté mais!")
            break
        else:
            print("\nOpção inválida. Escolha 1, 2 ou 3.\n")

    conexao.close()


if __name__ == "__main__":
    main()
