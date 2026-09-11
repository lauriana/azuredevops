# PARTE 2: Atividades Práticas — Projeto Loja com Azure Boards e Repos

**Tempo:** 1h30 (o restante da oficina Nível 1)

**Pré-requisito:** ter concluído o [Setup Inicial](../setup-inicial/README.md) — conta Azure, ferramentas instaladas, banco de dados criado, fork do projeto loja clonado.

> 👥 Se der, sente perto de alguém — comparar o progresso de vez em quando ajuda a pegar travas mais rápido do que resolver tudo sozinho.

---

## 📌 O que você vai fazer

Você não vai só seguir um passo a passo técnico — vai **planejar e rastrear o próprio trabalho como um time DevOps faria**, usando:

- **Azure Boards**: quadro com Épico → Issues → Tasks, movidas conforme você avança
- **Azure Repos**: código do projeto loja versionado, com commits vinculados às tarefas
- O **Azure SQL Database**, já criado no Setup Inicial

```
Atividade 1: Criar o Board (Épico + Issues + Tasks)      → 15 min
Atividade 2: Trazer o código para o Azure Repos          → 10 min
Atividade 3: Conectar a aplicação ao banco (.env)        → 10 min
Atividade 4: Criar a tabela produtos no banco             → 10 min
Atividade 5: Cadastrar um produto (a atividade principal) → 15 min
Atividade 6: Encerramento e Pull Request                  → 10 min
```

Depois destas atividades, se quiser ir mais fundo no Azure DevOps como ferramenta de gestão (sprints, relatórios, métricas), veja o módulo complementar **[Azure DevOps na Prática](./azure-devops-na-pratica.md)**.

---

## ATIVIDADE 1 — Criar o Board (15 min)

*Por que isso importa: em um time real, quase todo trabalho começa sendo quebrado em tarefas rastreáveis — não direto no código.*

### 1.1 Organização e Projeto

1. Acesse https://dev.azure.com e crie sua **Organização** (se ainda não tiver uma)
2. Crie um novo **Projeto Privado** — sugestão de nome: `projeto-loja`

### 1.2 Criar o backlog

Use o processo **Basic** (Épico → Issue → Task). No Board do projeto, crie:

- [ ] 1 **Epic**: `Projeto Loja - Cadastro de Produtos`
- [ ] 4 **Issues**, todas dentro desse Epic:
  1. `Preparar repositório e ambiente local`
  2. `Conectar a aplicação ao banco (.env)`
  3. `Criar a tabela produtos no banco`
  4. `Cadastrar e validar um produto`

> 💡 Cada Issue vira uma seção abaixo. Dentro dela, crie as Tasks listadas — isso é o que você vai arrastar de **A Fazer** → **Em Andamento** → **Concluído** ao longo da oficina.

**Critério de aceite:** o Board mostra o Epic e as 4 Issues na coluna "A Fazer".

> 👥 Checkpoint rápido: compare seu Board com o de alguém perto de você — os nomes do Epic e das Issues batem?

---

## ATIVIDADE 2 — Trazer o código para o Azure Repos (10 min)

*Por que isso importa: hoje quase todo código de verdade mora num repositório com histórico — trazer o projeto para lá é o primeiro passo antes de qualquer mudança.*

Corresponde à **Issue 1**.

- [ ] No projeto Azure DevOps, abra **Repos → Files → Import repository**
- [ ] Cole a URL do **seu fork** no GitHub (ex.: `github.com/SEU-USUARIO/project-devops-minicurso.git`)
- [ ] Confirme a importação — o histórico de commits do fork é preservado
- [ ] Crie uma branch a partir de `main`: `feature/1-preparar-ambiente`
- [ ] Clone o repositório **do Azure Repos** (não mais do GitHub) para uma pasta local
- [ ] Copie `database.py` e `main.py` da pasta [`codigo-sqlserver/`](./codigo-sqlserver/) para dentro de **`src/`**, substituindo os originais (o projeto original só fala com MySQL) — veja o [README daquela pasta](./codigo-sqlserver/README.md) para o passo a passo

**Critério de aceite:** o repositório aparece em Repos → Files; você tem uma cópia local clonada do Azure Repos com `src/main.py` e `src/database.py` adaptados para Azure SQL Database.

---

## ATIVIDADE 3 — Conectar a aplicação ao banco (10 min)

*Por que isso importa: nunca colocar senha ou chave direto no código é uma das regras de segurança mais básicas do mercado — é para isso que existe o `.env`.*

Corresponde à **Issue 2**.

- [ ] Copie `.env.example` para `.env`
- [ ] Preencha as 4 variáveis com os dados do banco **que você criou no Setup Inicial**

Variáveis lidas por `src/database.py`:
```
DB_HOST=seu-servidor.database.windows.net
DB_USER=seu_usuario_admin
DB_PASSWORD=sua_senha
DB_NAME=loja
```

> ⚠️ Os nomes das variáveis são **sempre estes 4**: `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` — não use `DB_PORT` nem `DB_DATABASE`, o `database.py` não lê esses nomes.

- [ ] Confirme que `.env` **não** aparece em `git status` (deve estar no `.gitignore`)
- [ ] Commit da branch vinculado ao work item:

```bash
git commit -m "Configura variaveis do banco (AB#2)"
```

> 💡 `AB#2` é o número da Issue 2 no Board — o Azure Repos cria o vínculo automaticamente. Use `Fixes AB#2` para o work item ser movido para Concluído quando o commit for enviado.

**Critério de aceite:** `.env` existe localmente com os 4 nomes corretos, não está versionado, e o commit aparece linkado à Issue 2.

---

## ATIVIDADE 4 — Criar a tabela `produtos` no banco (10 min)

*Por que isso importa: toda aplicação real depende de um banco de dados estruturado corretamente antes de rodar — é o alicerce que vem antes do código.*

Corresponde à **Issue 3**. Abra o VS Code, conecte-se ao seu banco com a extensão mssql, e rode o SQL abaixo.

> 💡 Primeira vez conectando a um banco pelo VS Code, ou primeira vez escrevendo um comando SQL? Veja **[Comandos Básicos](../comandos-basicos.md)** antes de continuar — explica `CREATE TABLE`, `SELECT`, e como rodar uma consulta na extensão.

```sql
CREATE TABLE produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);
```

(no Azure SQL Database o banco `loja` já foi escolhido/criado no momento em que você criou o recurso no Setup Inicial — não existe um comando `CREATE DATABASE` a rodar aqui dentro dele, você já está conectado nele.)

- [ ] Valide as colunas: **`id`, `nome_produto`, `valor`**, nem uma a mais nem com nomes diferentes — expanda **Databases → loja → Tables → produtos → Columns** no painel da extensão mssql, ou rode:
```sql
SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'produtos';
```

**Critério de aceite:** a tabela existe com exatamente essas 3 colunas — são as que `main.py` espera encontrar.

---

## ATIVIDADE 5 — Cadastrar um produto (15 min) 🎯

*Por que isso importa: é o momento em que tudo se conecta — código, banco e infraestrutura funcionando juntos, exatamente como em produção.*

Esta é a atividade principal: colocar o CRUD para funcionar de ponta a ponta. Corresponde à **Issue 4**.

### 5.1 Rodar a aplicação

> 💡 Não lembra onde digitar esse comando? É no **terminal integrado do VS Code** (`` Ctrl+` `` ou menu Terminal → New Terminal). Primeira vez, ou voltando ao projeto depois de um tempo? Veja **[Comandos Básicos](../comandos-basicos.md)**.

A partir da **raiz** do projeto (não de dentro de `src/`):

```bash
python -m src.main
```

> ⚠️ O código do projeto loja fica dentro de uma pasta `src/` (`src/main.py`, `src/database.py`), então `python main.py` ou `python src/main.py` **não funcionam** — dão erro de import. `python -m src.main` é o comando certo.

Deve aparecer o menu:
```
===========================================
=      (1) - Cadastrar produto            =
=      (2) - Visualizar produtos          =
=      (3) - Sair                         =
===========================================
```

### 5.2 Cadastrar seu primeiro produto

- [ ] Escolha a opção **1**
- [ ] Informe um nome (ex.: `Mouse Sem Fio`) e um valor (ex.: `89.90`)
- [ ] Confirme que aparece: `Produto cadastrado com sucesso!`

### 5.3 Validar de duas formas

- [ ] Pela própria aplicação: opção **2** → o produto deve aparecer na lista
- [ ] Direto no banco, pelo VS Code:

```sql
SELECT * FROM produtos;
```

### 5.4 Desafio extra (se sobrar tempo)

- [ ] Cadastre mais 2 produtos pela opção 1
- [ ] Rode `SELECT nome_produto, valor FROM produtos WHERE valor > 50;`
- [ ] Commit do que mudou: `git commit -m "Valida cadastro de produto (AB#4)"`

**Critério de aceite:** um produto cadastrado por você na opção 1 aparece tanto na opção 2 do programa quanto em um `SELECT * FROM produtos` direto no banco.

> 👥 Checkpoint rápido: mostre para alguém perto de você que o produto cadastrado aparece tanto na opção 2 quanto no `SELECT`. Ajudar o colega a chegar lá também conta.

---

## ATIVIDADE 6 — Encerramento e Pull Request (10 min)

*Por que isso importa: é exatamente o que acontece toda vez que alguém abre um Pull Request numa empresa de verdade — revisão antes de integrar.*

- [ ] Abra um **Pull Request** de cada branch de trabalho de volta para `main`
- [ ] Revise o diff — confirme que `.env` **não** aparece nas mudanças
- [ ] Faça o merge dos Pull Requests
- [ ] Mova as 4 Issues para **Concluído** no Board
- [ ] **Importante:** exclua ou marque para exclusão o Azure SQL Database usado, para não deixar recursos de teste ativos à toa

**Critério de aceite:** Board com as 4 Issues em "Concluído"; nenhum recurso de teste continua ativo na sua assinatura.

---

## O QUE VOCÊ TEM AGORA

- ✅ Board no Azure DevOps com o histórico completo do que foi feito
- ✅ Código do projeto loja versionado no Azure Repos, com commits linkados às tarefas
- ✅ Azure SQL Database na nuvem, com a tabela `produtos` no formato correto
- ✅ Aplicação funcionando de ponta a ponta — você cadastrou um produto de verdade
- ✅ Prática real do ciclo: **item de backlog → branch → commit → Pull Request → item concluído**

---

## 🚀 PRÓXIMOS PASSOS

- Quer entender melhor o Azure DevOps como ferramenta de gestão — sprints, relatórios, métricas? → **[Azure DevOps na Prática](./azure-devops-na-pratica.md)**
- Nível 2 - Integração Contínua (CI): onde o código se encontra com a automação — os commits que você acabou de fazer manualmente vão passar a disparar pipelines automáticos.

---

**Parabéns por chegar até aqui! 🚀**
