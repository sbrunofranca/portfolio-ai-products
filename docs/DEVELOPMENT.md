# 🛠️ Development Guide

Guia completo para configurar seu ambiente de desenvolvimento local para o **Portfolio AI Products**.

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Setup Local](#setup-local)
3. [Estrutura de Projetos](#estrutura-de-projetos)
4. [Desenvolvimento](#desenvolvimento)
5. [Testes](#testes)
6. [Pre-commit Hooks](#pre-commit-hooks)
7. [Troubleshooting](#troubleshooting)

---

## ✅ Pré-requisitos

- **Python**: 3.11+ (testado em 3.11, 3.12, 3.13)
- **pip**: 23.0+
- **Git**: 2.30+
- **Make**: (opcional, para comandos do Makefile)
- **Docker**: (opcional, para reproducibilidade)

### Verificar Versões

```bash
python --version      # Python 3.11.x
pip --version        # pip 23.x+
git --version        # git 2.30+
```

---

## 🚀 Setup Local

### 1. Clone do Repositório

```bash
git clone https://github.com/sbrunofranca/portfolio-ai-products.git
cd portfolio-ai-products
```

### 2. Escolha um Projeto

Cada projeto é independente. Escolha um para começar:

```bash
cd agent-assist-copilot        # Assistência de agentes
# ou
cd supply-chain-copilot        # Supply chain
# ou
cd analytics-ai-copilot        # Análise de dados
# ou
cd autonomous-supply-chain-ai  # Supply chain autônoma
```

### 3. Crie um Virtual Environment

```bash
# Criar venv
python -m venv venv

# Ativar (macOS/Linux)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate
```

### 4. Instale Dependências

```bash
# Dependências de produção
pip install -r requirements.txt

# Dependências de desenvolvimento (recomendado)
pip install -r requirements-dev.txt

# Ou usando o arquivo moderno (experimental):
pip install -e ".[dev]"  # usa pyproject.toml
```

### 5. Configure Variáveis de Ambiente

```bash
# Copiar template
cp .env.example .env

# Editar com suas credenciais
nano .env  # ou editor favorito
```

**Variáveis necessárias:**

```env
# Anthropic / Claude API
ANTHROPIC_API_KEY=sk_..._sua_chave_aqui

# Outras APIs (se usadas)
GROQ_API_KEY=gsk_...
DATABASE_URL=...

# Ambiente
DEBUG=False
ENVIRONMENT=development
```

### 6. Setup Pre-commit Hooks

```bash
# Instalar hooks
pre-commit install

# Testar em todos os arquivos (primeira vez)
pre-commit run --all-files
```

---

## 📁 Estrutura de Projetos

### Padrão Moderno

Cada projeto segue esta estrutura:

```
{project}/
├── src/{project_name}/         # Código principal
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/                 # Data models
│   ├── services/               # Business logic
│   ├── utils/                  # Utilities
│   ├── api/                    # FastAPI routes (se aplicável)
│   └── agents/                 # AI agents (se aplicável)
├── tests/                      # Testes
│   ├── __init__.py
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── conftest.py             # Pytest fixtures
├── docs/                       # Documentação local
├── pyproject.toml              # Configuração moderna (PEP 517)
├── requirements.txt            # Dependências de produção
├── requirements-dev.txt        # Dependências de desenvolvimento
├── pytest.ini                  # Configuração do pytest
├── Makefile                    # Comandos úteis
├── .env.example                # Template de variáveis
└── README.md                   # Documentação do projeto
```

### Imports

**Correto:**

```python
# Relativo ao src/
from src.project_name.models import User
from src.project_name.services import UserService

# Ou se instalado com pip install -e .
from project_name.models import User
```

---

## 🔨 Desenvolvimento

### Rodando a Aplicação

```bash
# FastAPI apps
python -m uvicorn src.main:app --reload

# Streamlit apps
streamlit run src/main.py

# Scripts standalone
python -m src.main
```

### Criar Novo Módulo

```bash
# Exemplo: criar novo serviço
mkdir -p src/{project_name}/services
touch src/{project_name}/services/__init__.py
touch src/{project_name}/services/my_service.py
```

**Template de serviço:**

```python
# src/project_name/services/my_service.py
from typing import Optional

class MyService:
    """Description of service."""

    def __init__(self):
        """Initialize service."""
        pass

    def do_something(self, param: str) -> Optional[str]:
        """Do something with param.

        Args:
            param: Input parameter

        Returns:
            Result or None
        """
        return None
```

### Código Limpo - Padrões

**Type hints:**

```python
from typing import List, Optional, Dict

def process_data(items: List[str]) -> Dict[str, int]:
    """Process items and return count."""
    return {item: 1 for item in items}
```

**Docstrings:**

```python
def calculate(a: int, b: int) -> int:
    """Calculate sum of a and b.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Raises:
        ValueError: If inputs are not integers
    """
    return a + b
```

---

## 🧪 Testes

### Estrutura de Testes

```
tests/
├── __init__.py
├── conftest.py                 # Fixtures compartilhadas
├── unit/
│   ├── test_models.py
│   ├── test_services.py
│   └── test_utils.py
└── integration/
    ├── test_api.py
    └── test_workflows.py
```

### Rodar Testes

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=src --cov-report=html

# Apenas tests/unit/
pytest tests/unit/

# Apenas um arquivo
pytest tests/unit/test_models.py

# Com output detalhado
pytest -vv

# Parar no primeiro erro
pytest -x
```

### Escrever Testes

```python
# tests/unit/test_services.py
import pytest
from src.project_name.services import MyService


@pytest.fixture
def service():
    """Fixture para MyService."""
    return MyService()


def test_service_init(service):
    """Test service initialization."""
    assert service is not None


def test_service_method(service):
    """Test service method."""
    result = service.do_something("test")
    assert result is not None
```

---

## 🪝 Pre-commit Hooks

### Verificações Automáticas

Antes de cada commit, executam-se:

```yaml
- trailing-whitespace: Remove espaços em branco
- end-of-file-fixer: Adiciona newline no final
- check-yaml: Valida YAML
- check-json: Valida JSON
- detect-private-key: Detecta credenciais
- isort: Ordena imports
- black: Formata código
- flake8: Linting
- mypy: Type checking
- bandit: Security checks
```

### Se Precisar Pular (NÃO RECOMENDADO)

```bash
# Pular pre-commit uma vez
git commit --no-verify

# Melhor: corrigir o problema!
pre-commit run --all-files
```

---

## 🔧 Comandos Úteis

### Makefile

```bash
# Setup completo
make setup

# Instalar dependências
make install
make install-dev

# Formatar código
make format

# Lint
make lint

# Testes
make test
make coverage

# Limpar arquivos temporários
make clean
make clean-all
```

### Tox (Multi-version Testing)

```bash
# Testar em Python 3.11, 3.12, 3.13
tox

# Apenas em py311
tox -e py311

# Lint + Type + Test
tox -e lint,type,coverage

# Limpar
tox -r
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named..."

**Solução:**

```bash
# Reinstalar dependências
pip install -r requirements.txt

# Ou com pip install -e .
pip install -e .
```

### "ANTHROPIC_API_KEY not found"

**Solução:**

```bash
# Verificar .env existe
ls -la .env

# Copiar .env.example
cp .env.example .env

# Editar com sua chave
nano .env
```

### Pre-commit falha

```bash
# Rodar manualmente para ver erro
pre-commit run --all-files

# Corrigir problemas
black src/ tests/
isort src/ tests/
```

### Testes falhando

```bash
# Limpar cache
pytest --cache-clear

# Rodar com verbose
pytest -vv

# Parar no primeiro erro
pytest -x
```

---

## 📚 Recursos

- [Python Docs](https://docs.python.org/)
- [Pytest Docs](https://docs.pytest.org/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Anthropic API](https://docs.anthropic.com/)
- [PEP 8 - Style Guide](https://pep8.org/)

---

**Última atualização**: 18 de Maio de 2026
