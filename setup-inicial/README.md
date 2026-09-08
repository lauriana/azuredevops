# SETUP INICIAL: Preparar Ambiente e Serviços - Nível 1

**Tempo:** ~45 minutos

**Pré-requisito:** Nenhum! Começamos do zero.

**Sistema operacional:** este guia cobre **Windows, macOS e Linux** em cada passo — siga a coluna do seu SO.

---

## 📌 O que este guia ensina

Este é um passo a passo **genérico**: conta na nuvem, ferramentas instaladas, escolha e criação de um banco de dados gerenciado, fork + clone de um repositório, ambiente preparado. É o que você precisa fazer antes de estudar **qualquer** projeto Python hospedado no GitHub — não só o do minicurso.

Para deixar tudo concreto, usamos como exemplo o **projeto loja** (`project-devops-minicurso`), usado na **Parte 2** deste minicurso. Depois de terminar aqui, você sabe repetir o mesmo processo para clonar qualquer outro projeto.

### 🗄️ Duas trilhas de banco de dados

O minicurso agora ensina os dois principais bancos relacionais gerenciados do Azure, lado a lado. Escolha **uma trilha** (ou faça as duas, se quiser comparar):

| | 🐬 Trilha MySQL | 🟦 Trilha SQL Server |
|---|---|---|
| Serviço Azure | Azure Database for MySQL – Flexible Server | Azure SQL Database (oferta gratuita) |
| Driver Python | `mysql-connector-python` | `pyodbc` + Driver ODBC 18 |
| Extensão VS Code | MySQL | SQL Server (mssql) |
| Sintaxe de tabela | `AUTO_INCREMENT` | `IDENTITY(1,1)` |
| Custo | Azure for Students (US$ 100 de crédito) | Oferta gratuita própria (100.000 vCore-segundos e 32 GB/mês, sem usar o crédito) |

As duas trilhas chegam ao **mesmo resultado** na Parte 2: cadastrar e visualizar produtos. A única coisa que muda é o serviço de banco e o driver de conexão. Marque desde já qual você vai seguir:

- [ ] Vou seguir a trilha **MySQL**
- [ ] Vou seguir a trilha **SQL Server**

---

## 📋 Passos

```
Passo 1: Conta Azure (estudante)              → 8 min
Passo 2: Instalar Git, Python, VS Code        → 10 min
Passo 3: Instalar o driver do seu banco       → 5 min
Passo 4: Criar o banco de dados no Azure      → 10 min
Passo 5: Fork + clonar o projeto              → 5 min
Passo 6: Preparar o ambiente Python           → 5 min
Passo 7: Testar                               → 5 min
```

---

## PASSO 1: Criar Conta Azure (estudante)

### 1.1 Acessar Azure para estudantes

1. Abra: https://azure.microsoft.com/pt-br/education/student/
2. Clique em **"Começar gratuitamente"**

### 1.2 Usar email do IFPR

```
seu_login@ifpr.edu.br
```

Se não tiver email IFPR:
- Peça ao coordenador do curso
- Ou use email pessoal + validação por SMS

### 1.3 Preencher formulário

- [ ] Email: seu_email@ifpr.edu.br
- [ ] Senha: crie uma forte
- [ ] País: Brasil
- [ ] Telefone: validar por SMS
- [ ] Data de nascimento

### 1.4 Validação

- Microsoft envia SMS → digite o código → pronto!

**Você recebe:**
- ✅ US$ 100 de crédito Azure (12 meses) — vale para a trilha MySQL
- ✅ Acesso à oferta gratuita do Azure SQL Database — não consome esse crédito, é um benefício à parte

---

## PASSO 2: Instalar Git, Python e VS Code

### 2.1 Git

| Windows | macOS | Linux |
|---|---|---|
| Baixe [git-scm.com/download/win](https://git-scm.com/download/win) e clique Next, Next, Next | `brew install git` (instale o [Homebrew](https://brew.sh) antes, se não tiver) | `sudo apt install git` (Ubuntu/Debian) ou `sudo dnf install git` (Fedora) |

**Verificar (todos os SOs):**
```bash
git --version
# Deve mostrar: git version 2.x.x
```

### 2.2 Python 3.10+

| Windows | macOS | Linux |
|---|---|---|
| Baixe em [python.org/downloads](https://www.python.org/downloads/). **Marque "Add Python to PATH"** e "Install pip" no instalador | `brew install python@3.12` — ou baixe em python.org | Geralmente já vem instalado. Se não: `sudo apt install python3 python3-pip python3-venv` |

**Verificar:**
```bash
python --version          # Windows
python3 --version         # macOS/Linux
# Deve mostrar: Python 3.10 ou superior

pip --version              # Windows
pip3 --version             # macOS/Linux
```

> 💡 Nos comandos deste guia, sempre que aparecer `python`/`pip`, use `python3`/`pip3` se estiver no macOS ou Linux e `python`/`pip` não funcionar.

### 2.3 VS Code

Baixe em [code.visualstudio.com](https://code.visualstudio.com/) (mesmo instalador para os três SOs).

**Instalar a extensão Python:**
1. Abra VS Code
2. Extensions (`Ctrl+Shift+X` no Windows/Linux, `Cmd+Shift+X` no Mac)
3. Procure **"Python"** (Microsoft) → Install

### 2.4 Conferir tudo de uma vez

```bash
git --version
python --version   # ou python3 --version
code --version
```

Deve aparecer versões de todas!

---

## PASSO 3: Instalar o Driver do Seu Banco

Siga **apenas a subseção da trilha que você escolheu.**

### 3A. Trilha MySQL — nada para instalar agora

O driver do MySQL é uma biblioteca Python (`mysql-connector-python`) que você instala junto com o projeto no Passo 6 — não precisa de nenhum instalador do sistema operacional.

Instale só a extensão do VS Code:
1. Extensions → procure **"MySQL"** (da Oracle ou da Weijan Chen) → Install

### 3B. Trilha SQL Server — instalar o Driver ODBC 18

O `pyodbc` (biblioteca Python que fala com o SQL Server) depende de um driver instalado no sistema operacional: o **Microsoft ODBC Driver 18 for SQL Server**.

**Windows:**
1. Baixe o instalador (x64) em: https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server
2. Rode o `.msi` → Next, Next, Finish

**macOS (Homebrew):**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"   # se ainda não tiver o Homebrew
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18
```

**Linux (Ubuntu/Debian):**
```bash
curl -sSL -O https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev
```

**Verificar a instalação (todos os SOs):**
```bash
python -m pip install pyodbc --break-system-packages   # Linux; no Windows/Mac, só "pip install pyodbc"
python -c "import pyodbc; print(pyodbc.drivers())"
# Deve listar 'ODBC Driver 18 for SQL Server' na lista
```

Instale também a extensão do VS Code:
1. Extensions → procure **"SQL Server (mssql)"** (Microsoft) → Install

---

## PASSO 4: Criar o Banco de Dados no Azure

Siga **apenas a subseção da trilha que você escolheu.** Os dois caminhos levam ao mesmo lugar: um servidor de banco na nuvem, pronto para receber a tabela `produtos` na Parte 2.

### 4A. Trilha MySQL — Azure Database for MySQL Flexible Server

1. No [portal Azure](https://portal.azure.com), busque **"Azure Database for MySQL flexible servers"** → **Create**
2. **Basics:** escolha sua assinatura (Azure for Students), crie um Resource Group novo, dê um nome ao servidor, escolha a região mais próxima
3. **Compute + storage:** deixe o tier "Burstable" (o mais barato) selecionado
4. **Authentication:** defina um usuário administrador e uma senha — **anote os dois**, vai precisar deles no `.env`
5. **Networking:** marque **"Allow public access from any Azure service"** e clique em **"Add current client IP address"**
6. **Review + create** → **Create** (leva de 5 a 15 minutos para provisionar)

**Critério de aceite:** o servidor aparece com status **"Available"** no portal.

### 4B. Trilha SQL Server — Azure SQL Database (oferta gratuita)

1. Abra https://aka.ms/azuresqlhub e clique em **"Start free"**
2. Confirme que aparece o aviso **"Free offer applied!"** e que o card de custo mostra **US$ 0/mês**
3. **Basics:** escolha sua assinatura, crie um Resource Group novo, dê um nome ao banco de dados (ex.: `loja`)
4. **Server:** clique em **"Create new"** — dê um nome de servidor único globalmente, escolha a região, e em **Authentication method** selecione **"Use SQL authentication"** — defina um login administrador e uma senha (**anote os dois**)
5. **Networking:** marque **"Allow Azure services and resources to access this server"** e **"Add current client IPv4 address"**
6. **Review + create** → **Create** (geralmente pronto em 1-2 minutos — bem mais rápido que o MySQL)

**Critério de aceite:** o banco aparece com status **"Online"**, e a tela de criação mostrou "Estimated cost: $0/month" antes de você confirmar.

> 💡 A oferta gratuita do Azure SQL Database renova todo mês e é por assinatura (não por aluno) — se toda a turma usar a mesma assinatura, combine com o instrutor para não passar de 10 bancos gratuitos nela.

---

## PASSO 5: Fork + Clonar o Projeto

Este é o passo que você repete **toda vez que quiser estudar um projeto de outra pessoa no GitHub**: primeiro um **fork** (sua cópia, na sua conta), depois **clone** do seu fork.

### 5.1 Fazer um fork do projeto loja

1. Abra: https://github.com/renanolv7/project-devops-minicurso
2. Clique em **Fork** (canto superior direito) → Confirme
3. Isso cria `github.com/SEU-USUARIO/project-devops-minicurso`

> 💡 Ao clonar outro projeto no futuro, é sempre este mesmo primeiro passo.

### 5.2 Clonar o seu fork

```bash
cd Documents        # Windows
cd ~                 # macOS/Linux

git clone https://github.com/SEU-USUARIO/project-devops-minicurso.git
cd project-devops-minicurso
```

(Troque `SEU-USUARIO` pelo seu usuário — é o **seu fork**, não o repositório original.)

### 5.3 Ver o que foi baixado

```bash
dir        # Windows
ls -la     # macOS/Linux
```

O projeto é enxuto:
```
project-devops-minicurso/
├── src/
│   ├── database.py    (conecta ao banco de dados)
│   └── main.py        (programa principal — CRUD de produtos)
├── .env.example       (modelo das variáveis de conexão)
├── .gitignore
└── README.md
```

> ⚠️ O código fica dentro da pasta `src/`, não na raiz. Isso importa na hora de rodar o programa (Passo 7 e Parte 2): o comando certo é `python -m src.main`, executado de dentro de `project-devops-minicurso/` — não `python main.py`.

> Se você for seguir a trilha **SQL Server**, vai substituir `src/database.py` e `src/main.py` pela versão adaptada da Parte 2 (pasta `codigo-sqlserver/`) — o projeto original só fala com MySQL.

---

## PASSO 6: Preparar o Ambiente Python

### 6.1 (Opcional, recomendado) Virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

O terminal deve mostrar `(venv)` no início da linha depois de ativar.

### 6.2 Instalar as dependências da sua trilha

**Trilha MySQL:**
```bash
python -m pip install mysql-connector-python python-dotenv
```

**Trilha SQL Server:**
```bash
python -m pip install pyodbc python-dotenv
```

**Pode levar 1-2 minutos...**

---

## PASSO 7: Testar

### 7.1 Ver o README do projeto

```bash
type README.md    # Windows
cat README.md      # macOS/Linux
```

### 7.2 Abrir no VS Code

```bash
code .
```

### 7.3 Entender a estrutura

```
project-devops-minicurso/
├── src/
│   ├── main.py        → menu do programa (cadastrar/visualizar produtos)
│   └── database.py    → conecta ao banco, lendo variáveis do .env
├── .env.example       → modelo a copiar para .env na Parte 2
└── README.md
```

Ainda **não** crie o `.env` nem rode o programa — isso é feito na Parte 2, depois de o banco de dados estar pronto. Quando for a hora, o comando é `python -m src.main` (executado da raiz do projeto — `python main.py` ou `python src/main.py` direto **não funcionam**, dão erro de import). Rodar agora, mesmo do jeito certo, dá erro de conexão (esperado, o `.env` ainda não existe).

---

## O QUE VOCÊ TEM AGORA

- ✅ Conta Azure criada
- ✅ Git, Python 3.10+ e VS Code instalados
- ✅ Driver e extensão do banco da sua trilha instalados
- ✅ Banco de dados criado no Azure (MySQL Flexible Server **ou** Azure SQL Database gratuito)
- ✅ Fork do projeto loja clonado
- ✅ Ambiente Python preparado
- ✅ **100% pronto para a Parte 2! 🚀**

---

## ⚠️ SE ALGO DER ERRADO

### "Git não encontrado"
Reinstale: Windows → [git-scm.com](https://git-scm.com/download/win) · macOS → `brew install git` · Linux → `sudo apt install git`

### "Python não encontrado"
```bash
python --version   # se falhar, tente:
python3 --version
```
Se persistir, reinstale marcando "Add to PATH" (Windows).

### "ModuleNotFoundError: No module named 'mysql'" (trilha MySQL)
```bash
python -m pip install mysql-connector-python python-dotenv
```

### "ModuleNotFoundError: No module named 'pyodbc'" ou "Can't open lib 'ODBC Driver 18...'" (trilha SQL Server)
O driver ODBC do sistema operacional está faltando, não é só o pacote Python. Refaça o Passo 3B para o seu SO e confirme com:
```bash
python -c "import pyodbc; print(pyodbc.drivers())"
```

### "Login failed" / "Cannot open server ... requested by the login"
- Trilha MySQL ou SQL Server: confira se seu IP atual está liberado no firewall do servidor (Passo 4) — seu IP pode ter mudado se você trocou de rede
- Confira usuário e senha no `.env` (veja a Parte 2)

### A conexão trava/demora e nunca dá erro nem sucesso (trilha SQL Server)
Isso costuma ser a **porta 1433 bloqueada pela rede** que você está usando (comum em redes de campus e corporativas) — diferente do firewall do Passo 4, que é do lado do Azure, esse bloqueio é do lado de fora, na rede local. O Azure SQL Database não tem um jeito de contornar isso usando outra porta.
- Teste em outra rede (dados móveis/hotspot do celular, por exemplo) para confirmar se é isso
- Se for uma rede da instituição, peça ao suporte de TI para liberar saída na porta **1433** para `*.database.windows.net`
- Mais detalhes: [guia de troubleshooting de conectividade do Azure SQL](https://azure.microsoft.com/en-us/blog/sql-azure-connectivity-troubleshooting-guide/)

### "Não consigo clonar" / "repository not found"
Confira se clonou a URL do **seu fork** (com o seu usuário), não do repositório original.

---

## 📞 DÚVIDAS?

- **Tem dúvida?** → [Abra uma Issue](../../issues/new?template=duvida.md)
- **Encontrou erro?** → [Reporte aqui](../../issues/new?template=bug.md)

### Exemplo de Issue boa

```
Título: "Erro ao instalar pyodbc no macOS"

Descrição:
Ao rodar python -c "import pyodbc", recebo:
Can't open lib 'ODBC Driver 18 for SQL Server' : file not found

Meu ambiente:
- OS: macOS 14 (Apple Silicon)
- Python: 3.12
- Segui o Passo 3B com brew install msodbcsql18

Já tentei:
- brew update && brew reinstall msodbcsql18
```

---

## 🚀 PRÓXIMO PASSO

Você está pronto para a **[Parte 2: Atividades Práticas](../nivel-1-atividades/README.md)** — lá você cria o Board no Azure DevOps, coloca o banco de dados de verdade no ar e cadastra seu primeiro produto.

---

## ✨ CHECKLIST FINAL

- [ ] Conta Azure criada
- [ ] Git, Python 3.10+ e VS Code instalados
- [ ] Driver/extensão do banco da sua trilha instalados (MySQL ou ODBC 18 + mssql)
- [ ] Banco de dados criado no Azure e com status Available/Online
- [ ] Fork do projeto loja clonado (do seu usuário, não do original)
- [ ] Dependências Python da sua trilha instaladas
- [ ] VS Code abre o projeto e mostra `src/main.py` e `src/database.py`

**Sim para tudo?** 🎉 **Vamos para a Parte 2!**

---

**Boa sorte! Você consegue! 💪**
