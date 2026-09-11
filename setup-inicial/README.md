# SETUP INICIAL: Preparar Ambiente e Serviços - Nível 1

**Tempo:** ~45 minutos

**Pré-requisito:** Nenhum! Começamos do zero.

**Sistema operacional:** este guia cobre **Windows, macOS e Linux** em cada passo — siga a coluna do seu SO.

---

## 📌 O que este guia ensina

Este é um passo a passo **genérico**: conta na nuvem, ferramentas instaladas, criação de um banco de dados gerenciado, fork + clone de um repositório, ambiente preparado. É o que você precisa fazer antes de estudar **qualquer** projeto Python hospedado no GitHub — não só o do minicurso.

Para deixar tudo concreto, usamos como exemplo o **projeto loja** (`project-devops-minicurso`), usado na **Parte 2** deste minicurso. Depois de terminar aqui, você sabe repetir o mesmo processo para clonar qualquer outro projeto.

O banco de dados usado neste minicurso é o **Azure SQL Database**, na oferta gratuita da Microsoft (100.000 vCore-segundos e 32 GB de armazenamento por mês) — não consome o crédito da sua conta de estudante. A conexão em Python é feita com `pyodbc` + o Driver ODBC 18, e a extensão do VS Code é a SQL Server (mssql).

---

## 📋 Passos

```
Passo 1: Conta Azure (estudante)              → 8 min
Passo 2: Instalar Git, Python, VS Code        → 10 min
Passo 3: Instalar o Driver ODBC 18            → 5 min
Passo 4: Criar o Azure SQL Database           → 10 min
Passo 5: Fork + clonar o projeto              → 5 min
Passo 6: Preparar o ambiente Python           → 5 min
Passo 7: Testar                               → 5 min
```

---

## PASSO 1: Criar Conta Azure (estudante)

### 1.1 Acessar a página do Azure for Students

1. Abra: https://azure.microsoft.com/pt-br/free/students
2. Clique em **"Comece gratuitamente"**

### 1.2 Entrar ou criar uma conta Microsoft

Antes de qualquer outra coisa, a Microsoft pede para você entrar com uma **conta Microsoft** — é a mesma conta usada no Outlook, Teams ou Xbox, não é uma conta "da Azure" separada:

- **Já tem uma conta Microsoft?** Entre normalmente com ela.
- **Não tem?** Clique em **"Criar uma!"** e crie uma conta nova. Recomendação: use seu e-mail `seu_login@ifpr.edu.br` como e-mail dessa conta — assim o próximo passo (verificação de aluno) já reconhece o domínio da instituição automaticamente.

> 💡 "Conta Microsoft" e "conta Azure" não são coisas diferentes — toda conta Azure é acessada através de uma conta Microsoft.

### 1.3 Verificar que você é aluno

Informe seu e-mail institucional:
```
seu_login@ifpr.edu.br
```

A Microsoft envia um link (ou código) de verificação para essa caixa de entrada — abra o e-mail e confirme.

Se não tiver email IFPR:
- Peça ao coordenador do curso
- Ou use email pessoal — nesse caso pode ser pedido um comprovante de matrícula (carteirinha, declaração)

### 1.4 Completar o cadastro

- [ ] País: Brasil
- [ ] Telefone: pode pedir validação por SMS
- [ ] Data de nascimento
- [ ] Aceitar os Termos de Uso e a Política de Privacidade

### 1.5 Pronto!

**Você recebe:**
- ✅ Acesso à oferta gratuita do Azure SQL Database — usado neste minicurso, sem consumir nenhum crédito
- ✅ US$ 100 de crédito Azure (12 meses) — não é necessário para este minicurso, mas fica disponível na sua conta para outros projetos

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

> 💡 Primeira vez usando o VS Code? Veja **[Comandos Básicos](../comandos-basicos.md)** — abrir pasta, paleta de comandos, terminal integrado, instalar extensão, tudo explicado com calma.

### 2.4 Conferir tudo de uma vez

```bash
git --version
python --version   # ou python3 --version
code --version
```

Deve aparecer versões de todas!

---

## PASSO 3: Instalar o Driver ODBC 18

O `pyodbc` (biblioteca Python que fala com o SQL Server) depende de um driver instalado no sistema operacional: o **Microsoft ODBC Driver 18 for SQL Server**.

**Windows:**
1. Baixe o instalador (x64) em: https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server
2. Rode o `.msi` → Next, Next, Finish

**macOS (Homebrew):**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"   # se ainda não tiver o Homebrew
brew tap microsoft/mssql-release https://github.com/microsoft/homebrew-mssql-release
brew update
HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18
```

> ⚠️ Reparou que é `microsoft` com letra minúscula na URL do `brew tap`? É de propósito — com maiúscula (como a própria documentação da Microsoft às vezes mostra) o Homebrew recusa com "Tap ... remote mismatch".
>
> Em versões mais novas do Homebrew, o comando de instalação pode recusar com **"Refusing to load formula ... from untrusted tap"**. Se isso acontecer, rode antes:
> ```bash
> brew trust microsoft/mssql-release
> ```
> e repita o `brew install`.

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

## PASSO 4: Criar o Azure SQL Database (oferta gratuita)

1. Abra https://aka.ms/azuresqlhub e clique em **"Start free"**
2. Confirme que aparece o aviso **"Free offer applied!"** e que o card de custo mostra **US$ 0/mês**
3. **Basics:** escolha sua assinatura, crie um Resource Group novo, dê um nome ao banco de dados (ex.: `loja`)
4. **Server:** clique em **"Create new"** — dê um nome de servidor único globalmente, escolha a região, e em **Authentication method** selecione **"Use SQL authentication"** — defina um login administrador e uma senha (**anote os dois**)
5. **Networking:** marque **"Allow Azure services and resources to access this server"** e **"Add current client IPv4 address"**
6. **Review + create** → **Create** (geralmente pronto em 1-2 minutos)

**Critério de aceite:** o banco aparece com status **"Online"**, e a tela de criação mostrou "Estimated cost: $0/month" antes de você confirmar.


---

## PASSO 5: Fork + Clonar o Projeto

Este é o passo que você repete **toda vez que quiser estudar um projeto de outra pessoa no GitHub**: primeiro um **fork** (sua cópia, na sua conta), depois **clone** do seu fork.

### 5.1 Fazer um fork do projeto loja

1. Abra: https://github.com/renanolv7/project-devops-minicurso
2. Clique em **Fork** (canto superior direito) → Confirme
3. Isso cria `github.com/SEU-USUARIO/project-devops-minicurso`

> 💡 Ao clonar outro projeto no futuro, é sempre este mesmo primeiro passo.

> 🆕 Primeira vez ouvindo falar em "fork", `git clone`, ou não sabe o que são esses comandos de terminal? Veja **[Comandos Básicos](../comandos-basicos.md)** antes de continuar.

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

> O projeto original só fala com MySQL — antes de rodar, você vai substituir `src/database.py` e `src/main.py` pela versão adaptada para Azure SQL Database (pasta `codigo-sqlserver/`), na Atividade 2 da Parte 2.

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

> ⚠️ Rode esses comandos **de dentro da pasta do projeto** (`project-devops-minicurso`, resultado do Passo 5) — é ali que a pasta `venv` deve ficar. Não copie nem mova uma `venv` já pronta de outro lugar (ex.: da sua pasta pessoal, de um projeto antigo) para dentro desta pasta: os caminhos internos dela ficam gravados no local onde foi criada, e uma `venv` movida costuma dar erro mesmo "ativando" sem problema aparente. Se precisar recomeçar, é mais seguro apagar e criar de novo (veja "SE ALGO DER ERRADO" abaixo).

### 6.2 Instalar as dependências

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
- ✅ Driver ODBC 18 e extensão mssql instalados
- ✅ Azure SQL Database criado (gratuito)
- ✅ Fork do projeto loja clonado
- ✅ Ambiente Python preparado
- ✅ **100% pronto para a Parte 2! 🚀**

---

## ⚠️ SE ALGO DER ERRADO

> 💡 Resumo de uma página só com os erros mais comuns: **[Guia Rápido de Erros Comuns](../guia-rapido-erros-comuns.md)**.

### "Git não encontrado"
Reinstale: Windows → [git-scm.com](https://git-scm.com/download/win) · macOS → `brew install git` · Linux → `sudo apt install git`

### "Python não encontrado"
```bash
python --version   # se falhar, tente:
python3 --version
```
Se persistir, reinstale marcando "Add to PATH" (Windows).

### Não apareceu `(venv)` depois de ativar, ou a venv dá erro estranho mesmo "ativada"
- Confirme que você está dentro da pasta do projeto antes de rodar `source venv/bin/activate` — rode `pwd` (macOS/Linux) ou `cd` sozinho (Windows) para conferir
- Se a pasta `venv` foi **copiada ou movida** de outro lugar (em vez de criada ali com `python3 -m venv venv`), os caminhos internos dela apontam para o lugar errado — isso dá erro de forma sutil (ex.: `pip install` parece funcionar mas instala no lugar errado, ou dá "No such file or directory"). Solução: apague e crie de novo, direto na pasta do projeto:
```bash
rm -rf venv          # Windows: rmdir /s venv
python3 -m venv venv
source venv/bin/activate
```

### "ModuleNotFoundError: No module named 'pyodbc'" ou "Can't open lib 'ODBC Driver 18...'"
O driver ODBC do sistema operacional está faltando, não é só o pacote Python. Refaça o Passo 3 para o seu SO e confirme com:
```bash
python -c "import pyodbc; print(pyodbc.drivers())"
```

### "Tap ... remote mismatch" ou "Refusing to load formula ... from untrusted tap" (macOS, Passo 3)
Isso é do Homebrew, não do driver em si:
- **remote mismatch:** você digitou (ou copiou de algum lugar) a URL do tap com `Microsoft` maiúsculo — o certo é `microsoft` minúsculo, como está no Passo 3
- **untrusted tap:** rode `brew trust microsoft/mssql-release` e repita o `brew install`

### "Login failed" / "Cannot open server ... requested by the login"
- Confira se seu IP atual está liberado no firewall do servidor (Passo 4) — seu IP pode ter mudado se você trocou de rede
- Confira usuário e senha no `.env` (veja a Parte 2)

### A conexão trava/demora e nunca dá erro nem sucesso
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
- Segui o Passo 3 com brew install msodbcsql18

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
- [ ] Driver ODBC 18 e extensão mssql instalados
- [ ] Azure SQL Database criado e com status Online
- [ ] Fork do projeto loja clonado (do seu usuário, não do original)
- [ ] Dependências Python instaladas (pyodbc, python-dotenv)
- [ ] VS Code abre o projeto e mostra `src/main.py` e `src/database.py`

**Sim para tudo?** 🎉 **Vamos para a Parte 2!**

---

**Boa sorte! Você consegue! 💪**
