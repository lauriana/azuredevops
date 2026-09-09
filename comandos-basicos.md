# Comandos Básicos do Minicurso — VS Code, SQL, Git e GitHub

Este é um guia de referência rápida para quem nunca usou o VS Code, escreveu um comando SQL, ou mexeu com Git/GitHub antes. Ele não substitui o Setup Inicial nem a Parte 2 — é para consultar quando aparecer um termo ou uma tela que você não reconhece.

---

## 🖥️ VS Code básico

### Abrir uma pasta de projeto

Sempre trabalhamos com uma **pasta** aberta no VS Code (não um arquivo solto).

- **Pelo terminal**, estando dentro da pasta do projeto: `code .` (o ponto significa "esta pasta")
- **Pelo próprio VS Code**: `File` → `Open Folder...` → escolha a pasta

> 💡 Se `code .` der erro `command not found`, o atalho de terminal do VS Code ainda não foi instalado. Abra o VS Code, aperte `Cmd+Shift+P` (Mac) ou `Ctrl+Shift+P` (Windows/Linux), digite **"Shell Command: Install 'code' command in PATH"** e confirme. Enquanto isso não estiver feito, abra pastas e arquivos direto pelo `File` do VS Code, sem problema.

### A paleta de comandos

O atalho mais importante do VS Code: `Cmd+Shift+P` (Mac) ou `Ctrl+Shift+P` (Windows/Linux). Abre uma caixa de busca onde você digita o **nome** do que quer fazer, em vez de procurar em menus. Vamos usar isso várias vezes neste minicurso — por exemplo, para conectar ao banco de dados (comandos que começam com "SQL Server:" ou "MySQL:").

### Terminal integrado

Um terminal *dentro* do VS Code, sem precisar abrir outro programa.

- Abrir: `` Ctrl+` `` (Mac e Windows/Linux) ou menu `Terminal` → `New Terminal`
- Ele já abre na pasta do projeto que você tem aberta — é o mesmo `cd` que você já faria manualmente, só que automático

### Instalar uma extensão

Extensões são "plugins" que ensinam o VS Code a fazer coisas novas — como falar com um banco de dados.

1. Clique no ícone de blocos empilhados na barra lateral esquerda (ou `Cmd+Shift+X` / `Ctrl+Shift+X`)
2. Digite o nome da extensão na busca (por exemplo, **"SQL Server (mssql)"** ou **"MySQL"**)
3. Clique em **Install** na que tiver o ícone da Microsoft (para mssql) ou o nome do autor indicado no guia
4. Pronto — não precisa reiniciar o VS Code, geralmente já fica disponível

### Editar e salvar um arquivo

- Clique no arquivo na barra lateral esquerda para abrir
- Edite normalmente, como em qualquer editor de texto
- Salvar: `Cmd+S` (Mac) ou `Ctrl+S` (Windows/Linux) — **sempre salve antes de rodar algo**, o VS Code não salva sozinho

### Conectar a um banco de dados e rodar uma consulta (extensão mssql, trilha SQL Server)

1. `Cmd+Shift+P` → digite **"SQL Server: Connect"** (ou clique no ícone da extensão na barra lateral)
2. Preencha servidor, usuário e senha quando for pedido (os mesmos dados do seu `.env`)
3. Crie um arquivo novo terminando em `.sql` (por exemplo, `teste.sql`)
4. Escreva seu comando SQL nele
5. Selecione o texto do comando e rode: clique com o botão direito → **"Execute Query"**, ou o ícone de "play" que aparece no canto do editor

(Para a trilha MySQL, o fluxo é o mesmo, só muda para a extensão MySQL e o comando na paleta começa com "MySQL:".)

---

## 🗄️ SQL básico

SQL é a linguagem para conversar com um banco de dados relacional (MySQL e SQL Server são dois "sotaques" dela — bem parecidos, com pequenas diferenças de sintaxe). Nós usamos só um punhado de comandos neste minicurso.

### O básico: tabelas, linhas e colunas

Uma tabela é como uma planilha: tem **colunas** (os campos, ex.: `nome_produto`, `valor`) e **linhas** (cada produto cadastrado é uma linha). O comando sempre termina com `;` (ponto e vírgula) — é assim que o banco sabe onde um comando acaba.

### `CREATE TABLE` — criar uma tabela

É o comando que usamos na Atividade 4 da Parte 2, uma única vez, para preparar o banco antes de rodar o programa:

```sql
CREATE TABLE produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,   -- SQL Server (no MySQL: AUTO_INCREMENT)
    nome_produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);
```

- `INT`, `VARCHAR(100)`, `DECIMAL(10,2)` são **tipos de dado**: número inteiro, texto de até 100 caracteres, número com casas decimais
- `PRIMARY KEY` marca a coluna que identifica cada linha de forma única
- `NOT NULL` significa "esse campo é obrigatório, não pode ficar vazio"
- `--` inicia um comentário (texto que o banco ignora, só para explicação humana)

### `SELECT` — consultar dados

Para ver o que já está cadastrado:

```sql
SELECT * FROM produtos;
```

O `*` significa "todas as colunas". Para ver só algumas:

```sql
SELECT nome_produto, valor FROM produtos;
```

Para filtrar com uma condição (usamos isso no desafio extra da Atividade 5):

```sql
SELECT nome_produto, valor FROM produtos WHERE valor > 50;
```

### `INSERT INTO` — adicionar uma linha

No minicurso, quem roda esse comando é o **próprio programa** (`main.py`, opção 1 do menu) — você não precisa digitá-lo à mão. Mas é bom reconhecer o que está acontecendo por trás:

```sql
INSERT INTO produtos (nome_produto, valor) VALUES ('Mouse Sem Fio', 89.90);
```

### Onde as duas trilhas mudam

| | 🐬 MySQL | 🟦 SQL Server |
|---|---|---|
| Coluna que numera sozinha | `AUTO_INCREMENT` | `IDENTITY(1,1)` |
| Criar um banco novo | `CREATE DATABASE loja;` (existe, roda antes das tabelas) | não existe — o banco já é o próprio recurso Azure SQL Database criado no Setup Inicial |
| Ver as colunas de uma tabela | `DESCRIBE produtos;` | consultar `sys.columns` ou o painel de tabelas da extensão mssql |

O resto (`SELECT`, `INSERT INTO`, `WHERE`) é **idêntico** nas duas trilhas — é por isso que dá para trocar de trilha na Atividade 5 e o resultado final é o mesmo.

---

## 🔀 Git básico

Git guarda o **histórico** do seu código — cada mudança salva vira um "commit", e você pode ir e voltar nesse histórico, comparar versões, e mandar/receber mudanças do GitHub ou do Azure Repos. Aqui está só o punhado de comandos que aparece no minicurso.

### Trazer um repositório para sua máquina

```bash
git clone https://github.com/usuario/nome-do-repo.git
cd nome-do-repo
```

`clone` copia o repositório inteiro (com todo o histórico) para uma pasta nova. Você só faz isso **uma vez** por repositório — depois é `pull` (veja abaixo) para atualizar.

### Ver o que mudou

```bash
git status
```

Mostra quais arquivos você alterou, criou ou apagou desde o último commit. É o comando que você mais vai rodar — sempre que estiver em dúvida do que está acontecendo, rode `git status`.

### Salvar uma mudança (commit)

Isso é sempre em **duas etapas**:

```bash
git add .              # 1. seleciona todos os arquivos alterados para o commit
git commit -m "Configura variaveis do banco (AB#2)"    # 2. salva como um "ponto na história", com uma mensagem
```

`git add .` seleciona *tudo* que mudou na pasta atual (o ponto significa "aqui"). Se quiser selecionar só um arquivo específico: `git add nome-do-arquivo`.

> 💡 O `AB#2` na mensagem do commit é o número da Issue no Board do Azure DevOps — é assim que o Azure Repos sabe vincular esse commit à tarefa (ver Atividade 3 da Parte 2).

### Enviar e trazer mudanças

```bash
git push origin nome-do-branch     # envia seus commits para o GitHub/Azure Repos
git pull origin nome-do-branch     # traz mudanças que já estão lá (de outra máquina, ou de outra pessoa)
```

`origin` é o "apelido" padrão do repositório remoto (GitHub ou Azure Repos) — você não costuma precisar mudar isso.

### Branches — trabalhar em uma cópia paralela

Um branch é uma "ramificação" do código, isolada da principal (`main`), para você mexer sem bagunçar o que já está funcionando.

```bash
git checkout -b feature/1-preparar-ambiente    # cria um branch novo E já muda para ele
git checkout main                               # volta para o branch principal
git branch                                      # lista os branches que existem localmente
```

### Ver o histórico

```bash
git log --oneline
```

Mostra os commits em ordem, um por linha, com o identificador curto de cada um. Útil para conferir se seu commit realmente foi salvo.

### Onde cada comando aparece no minicurso

| Comando | Onde |
|---|---|
| `git clone` | Setup Inicial, Passo 5 — clonar seu fork do projeto loja |
| `git checkout -b` | Parte 2, Atividade 2 — criar o branch de trabalho |
| `git add` / `git commit` | Parte 2, Atividades 3 e 5 — salvar mudanças vinculadas a uma Issue (`AB#N`) |
| `git push` | Parte 2, Atividade 6 — enviar o branch para abrir o Pull Request |
| `git status` | o tempo todo — é seu comando de "onde eu estou?" |

---

## 🐙 GitHub básico

Git é a ferramenta (roda no seu computador); **GitHub** é o site onde os repositórios ficam hospedados na nuvem, com uma interface visual por cima do Git.

### Repositório (repo)

É a "pasta do projeto" hospedada no GitHub — com todo o histórico do Git, o código, e normalmente um `README.md` explicando do que se trata.

### Fork — sua própria cópia de um projeto

Um **fork** cria uma cópia completa de um repositório de outra pessoa, dentro da sua própria conta do GitHub (`github.com/SEU-USUARIO/nome-do-repo`). É o que você faz no Setup Inicial com o projeto loja, antes de clonar:

1. Abra o repositório original no GitHub
2. Clique no botão **Fork** (canto superior direito)
3. Confirme — em poucos segundos aparece a cópia em `github.com/SEU-USUARIO/...`

Só depois do fork você clona (`git clone`) — sempre a URL do **seu** fork, não a do repositório original. É assim que você consegue enviar (`git push`) suas próprias mudanças sem precisar de permissão no projeto de outra pessoa.

### Duas coisas com o mesmo nome: "Issue"

Isso confunde bastante gente no começo — **"Issue" existe em dois lugares diferentes neste minicurso**, e não são a mesma coisa:

| | Issue do **GitHub** | Issue do **Azure Boards** |
|---|---|---|
| Para quê | Dúvidas, bugs, sugestões sobre o material do curso | Uma tarefa do seu trabalho (ex.: "Conectar a aplicação ao banco") |
| Onde | Aba "Issues" do repositório no GitHub | Board do seu projeto no Azure DevOps |
| Quando você usa | Se tiver dúvida ou achar um erro no material (ver seção "Dúvidas?" do README) | Durante toda a Parte 2, é o seu quadro de trabalho |

Quando o guia fala em "mover a Issue para Concluído" ou "vincular o commit com `AB#2`", é sempre a Issue do **Azure Boards**. As Issues do GitHub são só para você (aluno) reportar problemas com o material do curso em si.

### Pull Request (PR)

Um Pull Request é um **pedido para juntar** as mudanças de um branch de volta no branch principal (`main`) — com uma tela mostrando exatamente o que mudou (o "diff"), para revisar antes de confirmar. Usamos isso duas vezes: uma vez no fork do GitHub (se você quiser contribuir de volta com o projeto original, opcional) e, principalmente, dentro do Azure Repos na Atividade 6 da Parte 2, onde um PR é o jeito de levar o código do seu branch de trabalho para o `main` do projeto.

---

## 🔗 Onde isso se encaixa no minicurso

- **Setup Inicial**, Passo 2.3: instalar o VS Code e a extensão Python
- **Setup Inicial**, Passo 3B: instalar a extensão SQL Server (mssql) — trilha SQL Server
- **Setup Inicial**, Passo 5.1: primeiro **Fork**, no GitHub
- **Setup Inicial**, Passo 5.2: primeiro `git clone`
- **Parte 2**, Atividade 2: primeiro `git checkout -b`
- **Parte 2**, Atividade 3: primeiro `git add` / `git commit` vinculado a uma Issue
- **Parte 2**, Atividade 4: usar `CREATE TABLE` pela primeira vez
- **Parte 2**, Atividade 5: usar `SELECT` para conferir o que o programa cadastrou
- **Parte 2**, Atividade 6: primeiro `git push` para abrir o Pull Request

Voltando para o [Setup Inicial](./setup-inicial/README.md) ou para a [Parte 2](./nivel-1-atividades/README.md)? Este guia continua aqui, um clique de distância, sempre que precisar.
