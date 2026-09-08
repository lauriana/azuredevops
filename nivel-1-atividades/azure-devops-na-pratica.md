# Azure DevOps na Prática — Backlog, Sprints, Boards e Métricas

**Tempo:** ~1h (módulo complementar, opcional dentro do Nível 1)

**Pré-requisito:** ter concluído pelo menos a [Atividade 1 da Parte 2](./README.md#atividade-1--criar-o-board-15-min) — um Board com 1 Epic e 4 Issues já criado no projeto `projeto-loja`.

---

## 📌 Por que este módulo existe

Nas atividades da Parte 2 você já **usou** o Azure Boards e o Azure Repos para tocar o projeto loja. Este módulo complementar olha para o Azure DevOps com outro objetivo: entender **como um time usaria a ferramenta de verdade**, dia a dia, para gerenciar o trabalho — não só para você entregar uma tarefa, mas para o time inteiro saber o que está sendo feito, quando, e o quanto falta.

Vamos usar o mesmo Board do projeto loja como laboratório, cobrindo, nesta ordem:

```
Parte 1: Organizar o backlog                    → 10 min
Parte 2: Estruturar e acompanhar sprints        → 15 min
Parte 3: Trabalhar com Boards (Kanban)          → 10 min
Parte 4: Acompanhar entregas                    → 10 min
Parte 5: Visualizar relatórios e métricas       → 10 min
Parte 6: Entender o fluxo de trabalho da ferramenta → 5 min
```

---

## PARTE 1 — Organizar o Backlog (10 min)

O **Backlog** é a lista priorizada de tudo o que o time pode fazer — diferente do **Board**, que mostra só o que está *em andamento agora*. É no backlog que se decide **o quê** fazer e **em que ordem**, antes de decidir **quando**.

### 1.1 Abrir o backlog

- [ ] No projeto `projeto-loja`, acesse **Boards → Backlogs**
- [ ] Confirme que está vendo o nível **Issues** (é o nível de trabalho do processo **Basic**, equivalente a "Stories" no processo Agile ou "Product Backlog Items" no Scrum)
- [ ] Você deve ver as 4 Issues criadas na Atividade 1 da Parte 2, todas dentro do Epic `Projeto Loja - Cadastro de Produtos`

### 1.2 Priorizar por arrastar-e-soltar

No Azure Boards, a **ordem das linhas no backlog é a prioridade** — não existe um campo "prioridade 1, 2, 3" separado que precise ser preenchido à parte (embora exista o campo `Priority`, o que importa para o time é a ordem visual).

- [ ] Arraste a Issue `Preparar repositório e ambiente local` para o topo — é sempre a primeira coisa que precisa ser feita
- [ ] Reordene as outras 3 na sequência que faz sentido para o fluxo (conectar banco → criar tabela → cadastrar produto)

### 1.3 Ver a estrutura pai/filho

- [ ] Clique no ícone de **View options** (canto superior direito do backlog)
- [ ] Ative **Parents** — agora cada Issue aparece agrupada sob o Epic `Projeto Loja`
- [ ] Ative **Planning** — um painel lateral aparece, mostrando as sprints do time (vamos usar isso na Parte 2)

**Critério de aceite:** as 4 Issues aparecem ordenadas por prioridade de execução, agrupadas visualmente sob o Epic.

---

## PARTE 2 — Estruturar e Acompanhar Sprints (15 min)

Uma **sprint** (no Azure DevOps, tecnicamente um **Iteration Path**) é um recorte de tempo fixo (ex.: 1 ou 2 semanas) para o qual você atribui um conjunto de itens do backlog. É o mecanismo que transforma "uma lista de tarefas" em "um plano de trabalho com prazo".

### 2.1 Definir as datas da sprint

- [ ] Acesse **Boards → Sprints** (você cai direto na aba **Backlog** da sprint atual, geralmente chamada `Sprint 1`)
- [ ] No topo da página, clique em **Set dates**
- [ ] Na janela **Edit iteration**, defina início e fim (sugestão: hoje até daqui 1 semana, para simular uma sprint curta de oficina)
- [ ] **Save and close**

> 💡 Se seu time precisar de várias sprints com datas diferentes, isso é feito em **Project Settings → Boards → Project configuration** (cria as sprints no nível do projeto) e depois em **Team configuration** (decide quais sprints esse time específico usa). Para o projeto loja, uma sprint já é suficiente.

### 2.2 Atribuir as Issues à sprint

Com o painel **Planning** ativado (Parte 1.3):

- [ ] Volte para **Boards → Backlogs**
- [ ] Arraste as 4 Issues, uma a uma, do backlog para a caixa da `Sprint 1` que aparece no painel lateral direito
- [ ] Repare que a caixa da sprint atualiza mostrando quantos itens foram planejados

Alternativa mais rápida: selecione as 4 Issues com `Ctrl+clique`, clique com o botão direito → **Move to iteration** → escolha `Sprint 1`.

### 2.3 Conhecer o Sprint Taskboard

- [ ] Acesse **Boards → Sprints → Taskboard**
- [ ] Você verá as 4 Issues como "linhas-mãe", cada uma podendo ter Tasks-filhas nas colunas **To Do / Doing / Done**
- [ ] Crie 1 Task rápida dentro da Issue `Conectar a aplicação ao banco (.env)`, por exemplo: `Testar variáveis do .env localmente` — isso simula como um time quebraria uma Issue em pedaços menores de trabalho diário

**Critério de aceite:** as 4 Issues estão dentro da `Sprint 1` com datas definidas, e pelo menos 1 Task existe no Taskboard.

---

## PARTE 3 — Trabalhar com Boards (Kanban) (10 min)

O **Board** (Kanban) é a visão do dia a dia: menos sobre planejamento, mais sobre **o que está travado, o que está andando, o que já saiu**.

### 3.1 Abrir o Board

- [ ] Acesse **Boards → Boards**
- [ ] Você verá as 4 Issues como cartões, distribuídos nas colunas **To Do**, **Doing**, **Done** (esses são os 3 estados do processo Basic)

### 3.2 Mover cartões conforme o trabalho avança

- [ ] Arraste `Preparar repositório e ambiente local` para **Doing** — na prática, é isso que você fez ao começar a Atividade 2 da Parte 2
- [ ] Conforme for concluindo as atividades da Parte 2 (ou já tiver concluído), mova as Issues correspondentes para **Done**

### 3.3 Personalizar colunas e limites de WIP (Work in Progress)

- [ ] Clique na engrenagem ⚙️ no canto do Board → **Column options**
- [ ] Repare no campo **WIP limit** de cada coluna — ele existe para forçar o time a **terminar** antes de **começar mais coisas** (ex.: limitar a coluna Doing a 2 itens por pessoa)
- [ ] Não precisa mudar nada agora — só reconheça onde essa configuração fica, pois é uma das primeiras coisas que um Scrum Master ajusta em um time real

**Critério de aceite:** o Board reflete o estado real do seu progresso nas atividades da Parte 2 (itens concluídos estão em Done).

---

## PARTE 4 — Acompanhar Entregas (10 min)

"Acompanhar entregas" é responder, a qualquer momento: **o que já foi entregue, o que falta, e o time vai terminar a tempo?**

### 4.1 Ver o progresso da sprint

- [ ] Em **Boards → Sprints → Taskboard**, observe a contagem no topo — Azure DevOps mostra quantos itens/tasks estão em cada estado
- [ ] Isso já é uma forma simples de acompanhamento de entrega: se no fim da sprint sobrar muita coisa em "To Do", a sprint não foi bem dimensionada

### 4.2 Usar uma Query para ver o que foi entregue

Queries são o jeito do Azure Boards responder perguntas específicas sobre os work items, sem depender só da visão do Board.

- [ ] Acesse **Boards → Queries → New query**
- [ ] Configure os filtros: `Work Item Type = Issue`, `State = Done`, `Iteration Path = Sprint 1`
- [ ] Rode a query — o resultado é exatamente "o que foi entregue nesta sprint"
- [ ] Salve a query com o nome `Entregas - Sprint 1`

### 4.3 Vincular entrega ao código (revisão)

Lembre da Atividade 3 da Parte 2: commits com `AB#2` ou `Fixes AB#2` no texto vinculam automaticamente o commit ao work item.

- [ ] Abra uma das Issues e role até a seção **Development** — se você já fez commits linkados, eles aparecem ali, provando a rastreabilidade **do código até o item do backlog**

**Critério de aceite:** você tem uma query salva mostrando os itens entregues, e consegue ver ao menos um commit vinculado a um work item.

---

## PARTE 5 — Visualizar Relatórios e Métricas (10 min)

Dashboards e widgets transformam os dados do Board em gráficos — úteis para reuniões de status sem precisar abrir Issue por Issue.

### 5.1 Criar um Dashboard

- [ ] Acesse **Overview → Dashboards**
- [ ] Clique em **New Dashboard**, nomeie como `Projeto Loja - Acompanhamento`
- [ ] **Create**

### 5.2 Adicionar o widget de Sprint Burndown

O gráfico de burndown mostra, dia a dia, quanto trabalho **restava** na sprint — a linha ideal é decrescente até zero no último dia.

- [ ] No dashboard, clique em **Edit → Add a widget**
- [ ] Procure por **Sprint Burndown**, adicione
- [ ] Configure para usar a `Sprint 1` e o campo de contagem (Count of Work Items, já que Issues do processo Basic normalmente não usam Story Points)

### 5.3 Adicionar um segundo widget: Cumulative Flow Diagram (CFD)

O CFD mostra, ao longo do tempo, quantos itens estão em cada coluna do Board (To Do / Doing / Done) — é o gráfico mais usado para identificar **gargalos** (uma faixa de cor que só cresce é sinal de itens empacando ali).

- [ ] **Add a widget → Cumulative Flow Diagram**
- [ ] Aponte para o Board do projeto loja
- [ ] **Save**

> 💡 Outros widgets do catálogo padrão valem a pena conhecer, mesmo sem configurar agora: **Velocity** (quanto o time entrega por sprint, ao longo de várias sprints — mais útil depois de 3+ sprints de histórico) e **Query Tile / Chart for Work Items** (transforma qualquer query salva, como a `Entregas - Sprint 1` da Parte 4, em um número ou gráfico no dashboard).

**Critério de aceite:** o Dashboard `Projeto Loja - Acompanhamento` existe com pelo menos 2 widgets configurados apontando para dados reais do seu projeto.

---

## PARTE 6 — Entender o Fluxo de Trabalho da Ferramenta (5 min)

Juntando tudo o que foi visto, o Azure Boards segue sempre o mesmo ciclo, não importa o tamanho do time:

```
 1. BACKLOG        →  o quê fazer, em que ordem
    (Boards > Backlogs)

 2. SPRINT          →  quando fazer (recorte de tempo + itens atribuídos)
    (Boards > Sprints)

 3. BOARD/TASKBOARD →  como está andando agora (estados: To Do → Doing → Done)
    (Boards > Boards / Taskboard)

 4. REPOS            → o trabalho vira código, linkado ao item (AB#N)
    (Repos > commits e Pull Requests)

 5. DASHBOARD         → visão consolidada para o time e stakeholders
    (Overview > Dashboards)
```

Cada Issue do projeto loja passou (ou vai passar) por esse ciclo completo: nasceu no backlog priorizado (Parte 1), foi puxada para uma sprint com prazo (Parte 2), andou pelas colunas do Board conforme o trabalho avançava (Parte 3), gerou commits rastreáveis (Parte 4), e apareceu consolidada em um gráfico (Parte 5).

Essa é a mesma lógica usada por times reais — a diferença entre a oficina e o dia a dia de um time não é a ferramenta, é a escala: mais pessoas, mais sprints, mais Epics em paralelo.

**Critério de aceite:** você consegue explicar, com suas palavras, por que um item passa por backlog → sprint → board → repos → dashboard, e não direto do backlog para "pronto".

---

## O QUE VOCÊ TEM AGORA

- ✅ Backlog do projeto loja priorizado e agrupado por Epic
- ✅ Uma sprint com datas definidas e os 4 itens de trabalho atribuídos a ela
- ✅ Prática de mover cartões no Board e organizar Tasks no Taskboard
- ✅ Uma query salva rastreando entregas da sprint
- ✅ Um Dashboard com burndown e cumulative flow diagram configurados
- ✅ Visão geral de como as peças do Azure DevOps se encaixam

---

## 🚀 PRÓXIMOS PASSOS

- Volte para as [Atividades da Parte 2](./README.md) se ainda não tiver concluído todas
- Nível 2 - Integração Contínua (CI): os commits linkados a work items que você viu na Parte 4 vão passar a disparar pipelines automáticos a cada push

---

**Parabéns por chegar até aqui! 🚀**
