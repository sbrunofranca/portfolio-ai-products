# 📦 Template para Novos Projetos

Este guia define a estrutura recomendada para novos projetos neste repositório.

---

## 📂 Estrutura de Diretórios

```
novo-projeto/
│
├── src/
│   └── novo_projeto/
│       ├── __init__.py
│       ├── main.py                 # Ponto de entrada principal
│       ├── config.py               # Configurações e settings
│       ├── constants.py            # Constantes do projeto
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   ├── user.py             # Modelos de dados (dataclasses, pydantic)
│       │   ├── schemas.py          # Schemas para validação (Pydantic)
│       │   └── enums.py            # Enumerações
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   ├── user_service.py     # Lógica de negócio
│       │   ├── auth_service.py
│       │   └── base_service.py     # Classe base reutilizável
│       │
│       ├── routes/                 # FastAPI routes (se usar FastAPI)
│       │   ├── __init__.py
│       │   ├── users.py
│       │   ├── auth.py
│       │   └── health.py           # Health check
│       │
│       ├── repositories/           # Acesso a dados (se usar BD)
│       │   ├── __init__.py
│       │   ├── base_repository.py
│       │   └── user_repository.py
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── decorators.py       # Decoradores customizados
│       │   ├── helpers.py          # Funções auxiliares
│       │   ├── validators.py       # Validadores customizados
│       │   └── logger.py           # Configuração de logging
│       │
│       ├── exceptions/
│       │   ├── __init__.py
│       │   └── custom_exceptions.py # Exceções customizadas
│       │
│       ├── middleware/             # Middlewares (se FastAPI)
│       │   ├── __init__.py
│       │   └── error_handler.py
│       │
│       └── external/               # Integrações externas
│           ├── __init__.py
│           ├── anthropic_client.py
│           └── database_client.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures
│   │
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   ├── test_services.py
│   │   └── test_utils.py
│   │
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_routes.py
│   │   └── test_database.py
│   │
│   └── fixtures/
│       ├── __init__.py
│       └── sample_data.py          # Dados para testes
│
├── docs/
│   ├── index.md                    # Documentação principal
│   ├── architecture.md             # Arquitetura
│   ├── api.md                      # Documentação de API
│   └── setup.md                    # Setup detalhado
│
├── migrations/                     # Migrações de banco de dados (Alembic)
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── scripts/
│   ├── __init__.py
│   ├── setup.py                    # Setup script
│   ├── migrate.py                  # Executar migrações
│   └── seed.py                     # Popular dados de teste
│
├── .env.example                    # Template de variáveis de ambiente
├── .env.test                       # Variáveis para testes
├── .github/
│   └── workflows/
│       ├── ci.yml                  # CI Pipeline
│       └── tests.yml               # Testes automatizados
│
├── requirements.txt                # Dependências principais
├── requirements-dev.txt            # Dependências de desenvolvimento
├── pyproject.toml                  # Configuração de projeto (Poetry/setuptools)
├── setup.py                        # Setup script (se não usar Poetry)
├── pytest.ini                      # Configuração do Pytest
├── .bandit                         # Configuração de security checks
├── mypy.ini                        # Configuração do mypy
├── .flake8                         # Configuração do flake8
│
├── README.md                       # Documentação do projeto
├── CHANGELOG.md                    # Histórico de mudanças
└── LICENSE                         # Licença do projeto
```

---

## 📝 Arquivos Mínimos Obrigatórios

### 1. `src/novo_projeto/__init__.py`

```python
"""
Projeto: Novo Projeto
Descrição: Breve descrição do projeto.
Versão: 0.1.0
Autor: Seu Nome
"""

__version__ = "0.1.0"
__author__ = "Seu Nome"

# Exports públicos
from .main import main

__all__ = ["main"]
```

### 2. `src/novo_projeto/main.py`

```python
"""Ponto de entrada principal da aplicação."""

import logging
from .config import settings

logger = logging.getLogger(__name__)


def main() -> None:
    """Função principal."""
    logger.info(f"Iniciando {settings.APP_NAME}")
    # Sua lógica aqui


if __name__ == "__main__":
    main()
```

### 3. `src/novo_projeto/config.py`

```python
"""Configurações da aplicação."""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Configurações da aplicação."""
    
    app_name: str = "Novo Projeto"
    debug: bool = False
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Carrega settings em cache."""
    return Settings()


settings = get_settings()
```

### 4. `requirements.txt`

```
# Essencial
anthropic==0.40.0
pydantic==2.5.0
pydantic-settings==2.1.0
python-dotenv==1.0.0

# Web (se aplicável)
fastapi==0.104.1
uvicorn[standard]==0.24.0

# Logging
python-json-logger==2.0.7
```

### 5. `requirements-dev.txt`

```
-r requirements.txt

# Testing
pytest==7.4.3
pytest-cov==4.1.0
pytest-asyncio==0.21.1
pytest-mock==3.12.0

# Code Quality
black==23.12.0
flake8==6.1.0
mypy==1.7.1
isort==5.13.2
bandit==1.7.5
pre-commit==3.5.0

# Development
ipython==8.18.1
```

### 6. `tests/conftest.py`

```python
"""Configurações e fixtures do Pytest."""

import pytest
from pathlib import Path

# Adiciona src ao path para imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


@pytest.fixture
def sample_data():
    """Fixture com dados de amostra."""
    return {
        "name": "Test",
        "value": 42
    }
```

### 7. `tests/unit/test_models.py`

```python
"""Testes para modelos."""

def test_something(sample_data):
    """Teste exemplo."""
    assert sample_data["value"] == 42
```

### 8. `README.md`

```markdown
# Novo Projeto

Descrição breve do projeto.

## 🚀 Quick Start

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📖 Documentação

Veja [docs/](./docs/) para mais informações.

## 🧪 Testes

```bash
pytest
pytest --cov=src
```

## 📝 Licença

MIT
```

### 9. `.env.example`

```
ENVIRONMENT=development
DEBUG=True
LOG_LEVEL=DEBUG
ANTHROPIC_API_KEY=sk_...
```

### 10. `pytest.ini`

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow tests
```

---

## 🚀 Setup de Novo Projeto

```bash
# 1. Crie a pasta
mkdir novo-projeto
cd novo-projeto

# 2. Crie a estrutura de diretórios
mkdir -p src/novo_projeto/{models,services,routes,utils,exceptions}
mkdir -p tests/{unit,integration,fixtures}
mkdir -p docs scripts

# 3. Crie os arquivos essenciais (use exemplos acima)
touch src/novo_projeto/__init__.py
touch src/novo_projeto/main.py
touch src/novo_projeto/config.py
touch tests/__init__.py
touch tests/conftest.py

# 4. Setup do ambiente
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 5. Setup de Git
cp ../.gitignore .gitignore
cp ../.editorconfig .editorconfig
git init
git add .
git commit -m "Initial commit: Project setup"

# 6. Pre-commit hooks
pre-commit install
```

---

## 🏗️ Padrões de Código

### Type Hints Obrigatórios

```python
# ✅ BOM
def process_user(user_id: int, name: str) -> User:
    """Processa um usuário."""
    ...

# ❌ RUIM
def process_user(user_id, name):
    ...
```

### Docstrings

```python
def complex_function(param1: str, param2: int) -> bool:
    """
    Descrição breve da função.
    
    Descrição mais detalhada, explicando comportamento complexo
    ou casos especiais se necessário.
    
    Args:
        param1: Descrição do primeiro parâmetro.
        param2: Descrição do segundo parâmetro.
    
    Returns:
        Descrição do que a função retorna.
    
    Raises:
        ValueError: Quando alguma condição não é atendida.
        TypeError: Quando tipos incorretos são passados.
    
    Example:
        >>> result = complex_function("test", 42)
        >>> print(result)
        True
    """
    ...
```

### Estrutura de Classes

```python
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """Modelo de usuário."""
    
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: Optional[str] = None
    
    def __post_init__(self):
        """Validação após inicialização."""
        if "@" not in self.email:
            raise ValueError(f"Email inválido: {self.email}")
    
    def get_display_name(self) -> str:
        """Retorna nome para exibição."""
        return self.name if self.is_active else f"{self.name} (Inativo)"
```

---

## ✅ Checklist para Novo Projeto

- [ ] Estrutura de diretórios criada
- [ ] Arquivos essenciais criados
- [ ] .env.example preenchido
- [ ] requirements.txt definido
- [ ] README.md escrito
- [ ] Testes básicos criados
- [ ] Type hints implementados
- [ ] Docstrings adicionadas
- [ ] Pre-commit hooks configurados
- [ ] CI/CD configurado

---

## 🔗 Referências

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Best Practices](https://docs.pytest.org/)
- [Type Hints Documentation](https://docs.python.org/3/library/typing.html)

---

*Última atualização: 18 de Maio de 2026*
