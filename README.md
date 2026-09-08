# Programa DevOps Azure IFPR

Boas Vindas! Aqui está todo o material dos minicursos de DevOps.

## 🎯 Objetivo

Aprender DevOps do zero com **Python + Git + Azure** — bancos de dados **MySQL** ou **SQL Server**, sua escolha.

Em 3 níveis. Sem teoria maçante. **Apenas prática!**

## 📚 Níveis

### Nível 1: Fundamentos de Devops, Cloud e Sustentabilidade (2h)
### Nível 2: Integração Contínua (CI)
### Nível 3: Entrega e Deploy (CD)

## 🚀 Como Começar

### Minicurso Nível 1: Fundamentos de Devops, Cloud e Sustentabilidade (2h)

O Nível 1 tem duas partes. Faça-as em ordem — a segunda depende do ambiente montado na primeira. Funciona em **Windows, macOS e Linux**, e você escolhe entre duas trilhas de banco de dados (pode até fazer as duas, se sobrar tempo):

| | 🐬 MySQL | 🟦 SQL Server |
|---|---|---|
| Serviço no Azure | Azure Database for MySQL | Azure SQL Database (oferta gratuita) |
| Custo | consome crédito da conta de estudante | grátis todo mês, sem cartão de crédito |
| Biblioteca Python | `mysql-connector-python` | `pyodbc` |

### Parte 1 — Setup Inicial (30 min)
[Clique aqui](./setup-inicial/README.md)

Você vai:
- Criar conta Azure (estudante)
- Instalar Git, Python, VS Code (instruções para Windows, macOS e Linux)
- Escolher sua trilha de banco (MySQL ou SQL Server) e criar o banco de dados na nuvem
- Fazer fork e clonar o projeto de exemplo (o mesmo padrão vale para clonar qualquer projeto seu de interesse depois)
- Preparar o ambiente Python

### Parte 2 — Atividades Práticas (1h30)
[Clique aqui](./nivel-1-atividades/README.md)

Você vai aprender, com tarefas específicas no **projeto loja**:
- Planejar o trabalho no **Azure Boards** (Épico → Issues → Tasks)
- Versionar o código no **Azure Repos**, com commits vinculados às tarefas
- Conectar a aplicação ao banco da sua trilha (MySQL ou SQL Server) e criar a tabela `produtos`
- Cadastrar um produto e validar de ponta a ponta

O código do projeto loja tem como base [renanolv7/project-devops-minicurso](https://github.com/renanolv7/project-devops-minicurso) (trilha MySQL original); a variante para a trilha SQL Server está em [`nivel-1-atividades/codigo-sqlserver/`](./nivel-1-atividades/codigo-sqlserver/).

### Complemento — Azure DevOps na Prática (~1h, opcional)
[Clique aqui](./nivel-1-atividades/azure-devops-na-pratica.md)

Depois (ou junto) das atividades da Parte 2, um mergulho no Azure DevOps como ferramenta de gestão de time, usando o próprio Board do projeto loja como laboratório:
- Organizar e priorizar o backlog
- Estruturar e acompanhar sprints
- Trabalhar com Boards (Kanban)
- Acompanhar entregas
- Visualizar relatórios e métricas (dashboards, burndown, cumulative flow)
- Entender o fluxo de trabalho da ferramenta, de ponta a ponta

## 💬 Dúvidas?

- **Tem dúvida?** → [Abra uma Issue](../../issues/new?template=duvida.md)
- **Completou desafio?** → [Compartilhe em Discussions](../../discussions)
- **Encontrou erro?** → [Reporte aqui](../../issues/new?template=bug.md)

## Equipe

### Coordenação
- **Profa. Lauriana Paludo** - Coordenadora do Projeto
  - Email: lauriana.paludo@ifpr.edu.br

### Alunos Participantes
| Nome | GitHub |
|------|--------|
| Renan Oliveira | [@renanolv](https://github.com/renanolv7) |
| Marcelo | [@marcelo](https://github.com/marcelo) |
| Michely | [@michely](https://github.com/michely) |
| Miguel | [@miguel](https://github.com/miguel) |

### Suporte
- 🐛 GitHub Issues: [Abrir Issue](../../issues)
- 💬 Discussions: [Ir para Discussions](../../discussions)


---

**Boa sorte na jornada DevOps! 🚀**
