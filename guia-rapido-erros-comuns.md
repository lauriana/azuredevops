# Guia Rápido de Erros Comuns

Resumo de uma página só, com os erros mais frequentes do minicurso e a solução rápida. Não substitui o [Setup Inicial](./setup-inicial/README.md), a [Parte 2](./nivel-1-atividades/README.md) nem os [Comandos Básicos](./comandos-basicos.md) — é para deixar aberto numa aba enquanto você trabalha.

| Sintoma | Solução rápida |
|---|---|
| "Git não encontrado" | Reinstalar: Windows → git-scm.com · macOS → `brew install git` · Linux → `sudo apt install git` |
| "Python não encontrado" | Testar `python3 --version`; reinstalar marcando "Add to PATH" no Windows |
| Não apareceu `(venv)` depois de ativar, ou dá erro estranho mesmo "ativada" | Confirme que está dentro da pasta do projeto; se a venv foi copiada de outro lugar (em vez de criada ali), apague e crie de novo direto na pasta do projeto: `python3 -m venv venv` |
| `ModuleNotFoundError: No module named 'pyodbc'` ou "Can't open lib 'ODBC Driver 18...'" | Falta o Driver ODBC do sistema — refaça o Passo 3 do Setup Inicial para o seu sistema operacional |
| "A SQL editor must have focus before you can execute this command" | Crie ou abra um arquivo `.sql`, clique dentro dele para dar foco, e só então rode "MS SQL: Connect" |
| Conexão com o banco trava sem erro nem sucesso | Porta 1433 bloqueada na rede local (comum em rede de campus) — teste no hotspot do celular, ou peça ao TI para liberar 1433 para `*.database.windows.net` |
| "Login failed" / "Cannot open server ... requested by the login" | Seu IP pode ter mudado (refaça a regra de firewall no Azure Portal); confira usuário e senha no `.env` |
| Erro de coluna ao cadastrar produto (nome não existe) | A tabela foi criada com a coluna `nome` em vez de `nome_produto` — recrie seguindo o SQL da Atividade 4 |
| "Não consigo clonar" / "repository not found" | Confirme que clonou a URL do **seu** fork (com o seu usuário do GitHub), não a do repositório original |

Ainda travado depois de tentar isso? Veja a seção completa **"⚠️ Se algo der errado"** do [Setup Inicial](./setup-inicial/README.md) ou abra uma [Issue](https://github.com/lauriana/azuredevops/issues/new?template=duvida.md) contando o que aconteceu.
