# 🛠️ PLANO DE AÇÃO - Reorganização & Padronização

**Projeto**: Portfolio AI Products
**Data**: 2026-05-18
**Objetivo**: Enterprise-grade organization and security

---

## 🔴 FASE 1: REMEDIAÇÃO CRÍTICA DE SEGURANÇA

### 1.1 Remover Credenciais Expostas do Git
**Ação**: Remove permanentemente .env files do histórico git
**Risco**: Alterará hashes de commits (git history rewrite)
**Comando**:
```bash
# Remover de forma segura usando git filter-repo
git clone --mirror <repo-url> portfolio-ai-products.git
cd portfolio-ai-products.git
git filter-repo --invert-paths --path '*.env'
git push --mirror <new-url>
```

**Status**: ⚠️ **REQUER CONFIRMAÇÃO** - operação destrutiva

### 1.2 Regenerar API Keys
**Ação**: Invalidar chave GROQ exposta e gerar nova
**Acesso**: Groq.com console
**Chave exposta**: `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`

**Status**: ⚠️ **REQUER AÇÃO MANUAL DO USUÁRIO**

### 1.3 Adicionar .env Files ao .gitignore
**Ação**: Garantir que .env files nunca sejam versionados
**Arquivo**: `.gitignore` (já contém, mas verificar + adicionar regras mais específicas)

```gitignore
# Variáveis de ambiente - NUNCA versionar
.env
.env.local
.env.*.local
.env.production.local
.env.development.local
!.env.example
```

**Status**: ✅ Pronto para implementação

### 1.4 Remover venv/ do Git
**Ação**: Remove directories virtuais do versionamento
**Comando**:
```bash
git rm -r --cached */venv/
git commit -m "chore: remove venv directories from git"
```

**Status**: ✅ Pronto para implementação

---

## 🟡 FASE 2: REORGANIZAÇÃO ESTRUTURAL

### 2.1 Centralizar Documentação
**Antes**:
```
root/
├── README.md
├── CONTRIBUTING.md
├── PROJECT_TEMPLATE.md
├── IMPLEMENTATION_CHECKLIST.md
├── PYTEST_FIX.md
└── .env.example
```

**Depois**:
```
root/
├── README.md (apresentação)
└── docs/
    ├── GETTING_STARTED.md (setup & quick start)
    ├── ARCHITECTURE.md (design & structure)
    ├── CONTRIBUTING.md (workflow & standards)
    ├── DEVELOPMENT.md (dev environment & tools)
    ├── API.md (API documentation)
    ├── DEPLOYMENT.md (deploy procedures)
    ├── SECURITY.md (security policies)
    └── TEMPLATES/
        ├── PROJECT_TEMPLATE.md
        ├── README_TEMPLATE.md
        └── CHECKLIST_TEMPLATE.md
```

**Benefício**: Documentação organizada e fácil de navegar

**Status**: ✅ Pronto para implementação

### 2.2 Reorganizar Scripts de Setup
**Antes**:
```
root/
├── apply-changes.py
├── apply-to-all-projects.py
├── clean-external-tests.py
├── complete-setup.py
├── reorganize-tests.py
└── fix-tests.sh
```

**Depois**:
```
root/
└── scripts/
    ├── README.md (documentação)
    ├── setup/
    │   ├── complete-setup.py (documented)
    │   └── apply-to-all-projects.py
    ├── maintenance/
    │   ├── clean-external-tests.py
    │   ├── reorganize-tests.py
    │   └── fix-tests.sh
    └── utils/
        └── apply-changes.py
```

**Benefício**: Scripts organizados, reutilizáveis, documentados

**Status**: ✅ Pronto para implementação

### 2.3 Padronizar Estrutura de Projetos
**Objetivo**: Todos os 4 copilots seguem o mesmo padrão

**Padrão Único**:
```
{project}/
├── src/{project_name}/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── services/
│   ├── utils/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   └── agents/
├── tests/
│   ├── __init__.py
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── docs/
│   ├── README.md
│   └── API.md
├── pyproject.toml
├── pytest.ini
├── .env.example
├── requirements.txt
├── requirements-dev.txt
└── Makefile
```

**Status**: ⚠️ Requer refactoring de código

### 2.4 Limpar Projetos Aninhados
**Exemplo problemático**:
```
analytics-ai-copilot/
├── ai-analytics-copilot/    ← por quê dois níveis?
│   ├── app/
│   ├── src/
│   └── README.md
├── app/                      ← duplicado?
├── src/                      ← duplicado?
```

**Ação**: Determinar se é necessário duplicação ou consolidar em um único nível

**Status**: ⚠️ Requer análise de propósito

---

## 🟢 FASE 3: PADRONIZAÇÃO DE CÓDIGO

### 3.1 Adicionar pyproject.toml
**Ação**: Substituir setup caótico de dependencies com padrão moderno (PEP 517/518)

**Template pyproject.toml**:
```toml
[build-system]
requires = ["setuptools>=65", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "agent-assist-copilot"
version = "0.1.0"
description = "Intelligent agent assistance copilot"
requires-python = ">=3.11"
authors = [{name = "Bruno França", email = "sbruno.franca@gmail.com"}]
dependencies = [
    "anthropic>=0.40.0",
    "fastapi>=0.104.1",
    "pydantic>=2.5.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.7.0",
    "isort>=5.12.0",
    "flake8>=6.0.0",
    "mypy>=1.4.1",
]

[tool.black]
line-length = 88
target-version = ["py311"]

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.11"
ignore_missing_imports = true
strict = false
```

**Benefício**:
- ✓ Padrão Python moderno
- ✓ Melhor compatibilidade com ferramentas
- ✓ Fácil gerenciar extras (dev, testing, etc)

**Status**: ✅ Pronto para implementação

### 3.2 Fixar Requirements
**Problema**:
```
aiobotocore @ file:///private/var/folders/nz/...  ✗ Não portável
anthropic==0.40.0  ✓ Fixado
```

**Ação**: Regenerar requirements.txt limpo

```bash
pip install pip-tools
pip-compile requirements.in --output-file=requirements.txt
```

**Status**: ✅ Pronto para implementação

### 3.3 Adicionar tox.ini
**Objetivo**: Testar em múltiplas versões Python (3.11, 3.12, 3.13)

```ini
[tox]
envlist = py311, py312, py313, lint, type

[testenv]
deps = -r{toxinidir}/requirements-dev.txt
commands = pytest {posargs}

[testenv:lint]
commands =
    black --check src tests
    isort --check-only src tests
    flake8 src tests

[testenv:type]
commands = mypy src
```

**Status**: ✅ Pronto para implementação

### 3.4 Adicionar GitHub Actions CI/CD
**Estrutura**:
```
.github/workflows/
├── ci.yml          (lint, test, coverage)
├── security.yml    (bandit, dependency checks)
└── release.yml     (changelog, release)
```

**Status**: ✅ Pronto para implementação

---

## 📝 FASE 4: DOCUMENTAÇÃO PADRONIZADA

### 4.1 Criar Templates Consistentes
**README.md Template para cada projeto**:
```markdown
# Project Name

## Overview
[2-3 sentença descrição]

## Stack
- Python 3.11+
- FastAPI 0.104
- Claude API (Anthropic)

## Quick Start
[Setup rápido]

## Architecture
[Diagrama / descrição]

## Development
[Como contribuir]

## Testing
[Como rodar testes]

## API Reference
[Endpoints / funções principais]

## Deployment
[Como fazer deploy]

## Contributing
[Link para CONTRIBUTING.md]
```

**Status**: ✅ Pronto para implementação

### 4.2 Criar SECURITY.md
**Conteúdo**:
- Políticas de .env
- Como reportar vulnerabilidades
- Scanning de dependências
- Secrets management
- API Key rotation procedures

**Status**: ✅ Pronto para implementação

### 4.3 Documentar Shared Assets
**Objetivo**: Explicar estrutura, como usar em outros projetos, padrões

**Status**: ✅ Pronto para implementação

---

## ⚙️ FASE 5: AUTOMAÇÃO

### 5.1 Melhorar Makefile
**Adicionar**:
```makefile
setup-all:
    for dir in */; do (cd $$dir && make setup); done

lint-all:
    for dir in */; do (cd $$dir && make lint); done

test-all:
    for dir in */; do (cd $$dir && make test); done

format-all:
    for dir in */; do (cd $$dir && make format); done
```

**Status**: ✅ Pronto para implementação

### 5.2 Atualizar pre-commit hooks
**Adicionar**:
```yaml
- repo: https://github.com/gitleaks/gitleaks
  hooks:
    - id: gitleaks
      name: gitleaks
      stages: [commit, push]

- repo: https://github.com/Lucas-C/pre-commit-hooks-bandit
  hooks:
    - id: python-bandit-vulnerability-check
```

**Status**: ✅ Pronto para implementação

---

## 📊 CRONOGRAMA SUGERIDO

| Fase | Tarefas | Tempo | Prioridade |
|------|---------|-------|-----------|
| 1 | Segurança (credenciais, venv) | 2-4h | 🔴 CRÍTICA |
| 2 | Reorganização (docs, scripts) | 4-6h | 🟡 ALTA |
| 3 | Padronização (pyproject, tox) | 4-6h | 🟡 ALTA |
| 4 | Documentação templates | 2-3h | 🟢 MÉDIA |
| 5 | Automação (CI/CD, hooks) | 6-8h | 🟢 MÉDIA |

**Total Estimado**: 18-27 horas
**Recomendação**: Fazer em 2-3 sprints

---

## ✅ CRITÉRIOS DE SUCESSO

- [ ] Zero credenciais no git
- [ ] 100% dos projetos com pyproject.toml
- [ ] CI/CD configurado e passando
- [ ] Documentação centralizada em /docs
- [ ] Todos scripts em /scripts com README
- [ ] Estrutura padronizada entre projetos
- [ ] Test coverage > 80%
- [ ] Pre-commit hooks passando
- [ ] Novos desenvolvedores conseguem setup em <30 minutos

---

## 🚦 PRÓXIMOS PASSOS

1. **Você confirma as ações?**
   - [ ] Sim, executar FASE 1 (segurança) imediatamente
   - [ ] Sim, executar FASES 1-2 (segurança + reorganização)
   - [ ] Sim, executar TODAS as fases
   - [ ] Não, apenas aconselhar
   - [ ] Customizar: [descreva]

2. **Git history rewrite?**
   - [ ] Sim, remover .env do histórico (⚠️ destrutivo)
   - [ ] Não, apenas remover arquivos e documentar

3. **Timeline?**
   - [ ] Tudo hoje (full sprint)
   - [ ] Hoje (FASE 1 crítica apenas)
   - [ ] Próximas 2 semanas (incremental)
