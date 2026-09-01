# SETUP INICIAL: Preparar Ambiente - Nível 1

**Tempo:** 30 minutos

**Pré-requisito:** Nenhum! Começamos do zero.

---

## 📌 5 PASSOS 

```
Passo 1: Conta Azure (estudante)     → 5 min
Passo 2: Instalar ferramentas        → 10 min
Passo 3: Clonar repositório          → 2 min
Passo 4: Preparar ambiente           → 5 min
Passo 5: Testar                      → 5 min
```

---

## PASSO 1: Criar Conta Azure (ESTUDANTE) 

### 1.1 Acessar Azure para estudantes

1. Abra: https://azure.microsoft.com/pt-br/education/student/
2. Clique em **"Começar gratuitamente"**

### 1.2 Usar email do IFPR

Use seu email institucional:
```
seu_login@ifpr.edu.br
```

Se não tiver email IFPR:
- Peça ao coordenador do curso
- Ou use email pessoal + SMS

### 1.3 Preencher formulário

- [ ] Email: seu_email@ifpr.edu.br
- [ ] Senha: crie uma forte
- [ ] País: Brasil
- [ ] Telefone: validar por SMS
- [ ] Data de nascimento

### 1.4 Validação

- Microsoft enviará SMS
- Digite código
- Pronto!

**Você recebe:**
- ✅ $100 de crédito Azure (12 meses)
- ✅ Acesso gratuito

---

## PASSO 2: Instalar Ferramentas - 10 min

### 2.1 Git

**Windows:**
- Baixe: https://git-scm.com/download/win
- Clique: Next, Next, Next
- Pronto!

**Mac:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt install git
```

**Verificar:**
```bash
git --version
# Deve mostrar: git version 2.x.x
```

### 2.2 Python 3.10+

**Baixe:** https://www.python.org/downloads/

**⚠️ IMPORTANTE na instalação:**
- [ ] Marcar: "Add Python to PATH"
- [ ] Marcar: "Install pip"

**Verificar:**
```bash
python --version 
# Deve mostrar: Python 3.10 ou superior

pip --version
# Deve mostrar: pip 21.x ou superior
```

### 2.3 VS Code

**Baixe:** https://code.visualstudio.com/

**Instalar extensão Python:**
1. Abra VS Code
2. Vá em: Extensions (Ctrl+Shift+X)
3. Procure: "Python"
4. Clique: Install (Microsoft)

**Pronto!**

### 2.4 Git + Python + VS Code

Verifique tudo funciona:

```bash
git --version
python --version
code --version
```

Deve aparecer versões de todas!

---

## PASSO 3: Clonar Repositório - 2 min

### 3.1 Abrir Terminal

**Windows:** PowerShell ou CMD
**Mac/Linux:** Terminal

### 3.2 Escolher pasta

```bash
# Windows
cd Documents

# Mac/Linux
cd ~
```

### 3.3 Clonar

```bash
git clone https://github.com/renanolv7/project-devops-minicurso.git
```

Vai criar pasta: `project-devops-minicurso`

### 3.4 Entrar na pasta

```bash
cd project-devops-minicurso
```

### 3.5 Ver o que foi baixado

```bash
# Windows
dir

# Mac/Linux
ls -la
```

Deve mostrar:
```
├── src/
├── tests/
├── .gitignore
├── README.md
├── requirements.txt
└── ...
```

---

## PASSO 4: Preparar Ambiente - 5 min

### 4.1 Criar Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**Após ativar, terminal deve mostrar:**
```
(venv) seu-usuario:project-devops-minicurso
```

### 4.2 Instalar dependências

```bash
pip install -r requirements.txt
```

**Vai instalar:**
- pyodbc (conexão SQL)
- pytest (testes)
- python-dotenv

**Pode levar 2-3 minutos...**

### 4.3 Pronto!

Seu ambiente está preparado.

---

## PASSO 5: Testar - 5 min

### 5.1 Ver README do projeto

```bash
# Windows
type README.md

# Mac/Linux
cat README.md
```

### 5.2 Listar arquivos importantes

```bash
# Ver estrutura
cd src
ls -la

# Deve ter:
# - main.py
# - database.py
```

### 5.3 Abrir no VS Code

```bash
# Voltar para raiz
cd ..

# Abrir VS Code
code .
```

**Pronto!** VS Code abre com o projeto!

### 5.4 Entender a estrutura

No VS Code, veja:
```
project-devops-minicurso/
├── src/
│   ├── main.py (programa principal)
│   └── database.py (conexão com SQL)
├── tests/ (testes)
├── requirements.txt (dependências)
├── .gitignore (o que Git ignora)
└── README.md (documentação)
```

---

## O QUE VOCÊ TEM AGORA

✅ Conta Azure criada ($100 crédito)
✅ Git instalado
✅ Python 3.10+ instalado
✅ VS Code instalado
✅ Repositório clonado
✅ Ambiente virtual criado
✅ Dependências instaladas
✅ Projeto aberto no VS Code
✅ **100% PRONTO PARA NÍVEL 1! 🚀**

---

## ⚠️ SE ALGO DER ERRADO

### "Git não encontrado"
```bash
# Reinstale Git
# Windows: https://git-scm.com/download/win
# Mac: brew install git
# Linux: sudo apt install git
```

### "Python não encontrado"
```bash
# Verificar PATH
python --version

# Se não funcionar:
python3 --version

# Se persistir, reinstale de https://python.org
# Marque "Add to PATH" na instalação!
```

### "ModuleNotFoundError"
```bash
# Ativar virtual environment!
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Depois instalar:
pip install -r requirements.txt
```

### "Permission denied" (Mac/Linux)
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

### "Não consigo clonar"
```bash
# Verificar conexão
ping github.com

# Se tiver problema de rede:
# 1. Verificar WiFi
# 2. Desabilitar VPN (se tiver)
# 3. Tentar novamente
```

---

## 📞 DÚVIDAS?

### Abrir Issue no GitHub

1. Vá em: github.com/seu-repo/issues
2. Clique: "New issue"
3. Escolha: "Dúvida"
4. Descreva o problema
5. Clique: "Submit"

**Você terá resposta em < 24h!**

### Exemplo de Issue boa

```
Título: "Erro ao instalar pyodbc"

Descrição:
Ao rodar pip install -r requirements.txt, recebo:
error: [XYZ]

Meu ambiente:
- OS: Windows 10
- Python: 3.9
- pip: 21.0

Já tentei:
- Reinstalar Python
- Rodar como admin
```

---

## 🚀 PRÓXIMO PASSO

1. Participe da **NÍVEL 1** (oficina 2h)
2. Você rodará código de verdade
3. Vai debugar no VS Code
4. Vai conectar a Azure SQL

---

## ✨ CHECKLIST FINAL

Antes de participar da oficina, confirme:

- [ ] Conta Azure criada
- [ ] Git instalado
- [ ] Python 3.9+ instalado
- [ ] VS Code instalado + extensão Python
- [ ] Repositório clonado
- [ ] Virtual environment criado
- [ ] Dependências instaladas
- [ ] VS Code abre o projeto
- [ ] Você consegue ver pasta `src/`

**Sim para tudo?** 🎉
**Você está 100% pronto! Até na oficina!**

---

**Boa sorte! Você consegue! 💪**
