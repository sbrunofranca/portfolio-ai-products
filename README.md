# 🤖 Portfolio AI Products

Suíte completa de produtos e copilots baseados em IA para otimização de negócios, com foco em automação, análise de dados e gerenciamento de supply chain.

---

## 📋 Projetos Inclusos

### 1. **Agent Assist Copilot** 
Assistente inteligente para suporte a agentes com automação de tarefas e insights em tempo real.
- **Status**: Em desenvolvimento
- **Stack**: Python, FastAPI, Claude API
- **Pasta**: [`/agent-assist-copilot`](./agent-assist-copilot)

### 2. **Analytics AI Copilot**
Plataforma de análise de dados com IA generativa para relatórios, previsões e dashboards inteligentes.
- **Status**: Em desenvolvimento
- **Stack**: Python, Data Science, Claude API
- **Pasta**: [`/analytics-ai-copilot`](./analytics-ai-copilot)

### 3. **Autonomous Supply Chain AI**
Sistema autônomo de gerenciamento de supply chain com otimização de rotas e previsão de demanda.
- **Status**: Em desenvolvimento
- **Stack**: Python, Machine Learning
- **Pasta**: [`/autonomous-supply-chain-ai`](./autonomous-supply-chain-ai)

### 4. **Supply Chain Copilot**
Assistente inteligente para operações de supply chain, logística e planejamento.
- **Status**: Em desenvolvimento
- **Stack**: Python, FastAPI, Claude API
- **Pasta**: [`/supply-chain-copilot`](./supply-chain-copilot)

### 5. **Shared Assets** 🔗
Biblioteca compartilhada de componentes, utilitários e integrações comuns entre projetos.
- **Inclui**: Clients de API, modelos de dados, funções utilitárias
- **Pasta**: [`/shared-assets`](./shared-assets)

---

## 🚀 Quick Start

### Pré-requisitos
- **Python** 3.11 ou superior
- **pip** ou **poetry** (opcional, mas recomendado)
- **Git**

### Setup Local - Por Projeto

Cada projeto é independente e segue o padrão de environment virtual:

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd portfolio-ai-products

# 2. Navegue até o projeto desejado
cd agent-assist-copilot

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Ative o ambiente
# No macOS/Linux:
source venv/bin/activate

# No Windows:
venv\Scripts\activate

# 5. Instale dependências
pip install -r requirements.txt

# 6. (Opcional) Instale dependências de desenvolvimento
pip install -r requirements-dev.txt

# 7. Configure variáveis de ambiente
cp .env.example .env
# Edite .env com suas credenciais
```

### Estrutura Geral

```
portfolio-ai-products/
├── agent-assist-copilot/          # Copiloto de assistência
│   ├── venv/                      # (não incluído no git)
│   ├── src/                       # Código fonte
│   ├── tests/                     # Testes
│   ├── requirements.txt           # Dependências
│   ├── requirements-dev.txt       # Ferramentas de dev
│   └── README.md                  # Documentação local
│
├── analytics-ai-copilot/          # Análise com IA
│   └── [mesmo padrão acima]
│
├── autonomous-supply-chain-ai/    # Supply chain autônoma
│   └── [mesmo padrão acima]
│
├── shared-assets/                 # Assets compartilhados
│   ├── clients/                   # Clients de API
│   ├── models/                    # Modelos de dados
│   ├── utils/                     # Funções utilitárias
│   └── __init__.py
│
├── supply-chain-copilot/          # Copiloto de supply chain
│   └── [mesmo padrão acima]
│
├── docs/                          # Documentação centralizada
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── CONTRIBUTING.md
│
├── .gitignore                     # Configuração Git
└── README.md                      # Este arquivo
```

---

## 📖 Documentação

### Documentação Geral
- **[CONTRIBUTING.md](./docs/CONTRIBUTING.md)** - Como contribuir
- **[ARCHITECTURE.md](./docs/ARCHITECTURE.md)** - Arquitetura do sistema
- **[API.md](./docs/API.md)** - Documentação de APIs

### Documentação por Projeto
Cada projeto contém seu próprio `README.md` com instruções específicas.

---

## 🔧 Desenvolvimento

### Estrutura Recomendada para Novos Projetos

```
novo-projeto/
├── src/
│   └── novo_projeto/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       └── models/
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── README.md
└── pyproject.toml (opcional, se usar poetry)
```

### Padrões de Código

- **Linguagem**: Python 3.11+
- **Linter**: `flake8`
- **Formatter**: `black`
- **Type Checking**: `mypy`
- **Testing**: `pytest`

### Executar Linting e Testes

```bash
# Dentro do projeto com venv ativado

# Linting
flake8 src/ tests/
black --check src/ tests/

# Formatting automático
black src/ tests/

# Type checking
mypy src/

# Testes
pytest
pytest --cov=src  # com cobertura

# Tudo junto
make test  # se houver Makefile
```

---

## 🔐 Variáveis de Ambiente

Cada projeto requer um arquivo `.env` para configurações sensíveis:

```bash
# Exemplo .env (nunca commitar!)
OPENAI_API_KEY=sk_...
DATABASE_URL=postgresql://...
DEBUG=False
ENVIRONMENT=development
```

Sempre use `.env.example` como template:
```bash
cp .env.example .env
```

---

## 🤝 Como Contribuir

1. **Fork** o repositório
2. **Crie uma branch** para sua feature: `git checkout -b feature/minha-feature`
3. **Faça commits** com mensagens descritivas: `git commit -am 'Adiciona nova feature'`
4. **Abra um Pull Request** com descrição clara
5. **Aguarde review** e feedback

### Commit Message Convention

```
tipo(escopo): descrição breve

corpo (opcional)
footer (opcional)

# Tipos: feat, fix, docs, style, refactor, perf, test, chore
# Exemplo: feat(auth): adiciona autenticação com OAuth
```

---

## 🐛 Reportar Issues

1. Verifique se já existe uma issue similar
2. Use templates de issue quando disponível
3. Inclua: passos para reproduzir, comportamento esperado vs atual
4. Anexe logs se relevante

---

## 📦 Dependências Externas

### Dependências Comuns
- **anthropic** - Cliente da API Claude
- **fastapi** - Framework web
- **pydantic** - Validação de dados
- **python-dotenv** - Gerenciamento de variáveis de ambiente

### Dependências de Desenvolvimento
- **pytest** - Testing framework
- **black** - Code formatter
- **flake8** - Linter
- **mypy** - Type checker

Veja `requirements.txt` e `requirements-dev.txt` em cada projeto para lista completa.

---

## 📊 Status dos Projetos

| Projeto | Status | Última Atualização |
|---------|--------|-------------------|
| Agent Assist Copilot | 🟡 Em Desenvolvimento | 2026-05-18 |
| Analytics AI Copilot | 🟡 Em Desenvolvimento | 2026-05-18 |
| Autonomous Supply Chain AI | 🟡 Em Desenvolvimento | 2026-05-18 |
| Supply Chain Copilot | 🟡 Em Desenvolvimento | 2026-05-18 |
| Shared Assets | 🟢 Estável | 2026-05-18 |

---

## 📚 Recursos Úteis

- [Claude API Documentation](https://docs.anthropic.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Best Practices](https://pep8.org/)
- [Git Workflow](https://git-scm.com/book/en/v2)

---

## 📝 Licença

[Especificar licença - ex: MIT, Apache 2.0]

---

## 👤 Autor

**Bruno França**
- Email: sbruno.franca@gmail.com
- GitHub: [@sbrunofranca](https://github.com/sbrunofranca)

---

## 🤝 Suporte

Encontrou um problema? 
- **Abra uma issue**: [Issues](../../issues)
- **Discussões**: [Discussions](../../discussions)
- **Email**: sbruno.franca@gmail.com

---

**Última atualização**: 18 de Maio de 2026  
**Versão**: 1.0.0-alpha
