.PHONY: help install dev lint format test coverage clean setup pre-commit

# Variáveis
VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PROJECT_NAME := portfolio-ai-products

# ============================================================
# HELP
# ============================================================
help:
	@echo "$(PROJECT_NAME) - Targets disponíveis:"
	@echo ""
	@echo "Setup:"
	@echo "  make setup          Cria venv e instala dependências"
	@echo "  make install        Instala dependências"
	@echo "  make install-dev    Instala dependências de desenvolvimento"
	@echo ""
	@echo "Desenvolvimento:"
	@echo "  make format         Formata código com black e isort"
	@echo "  make lint           Executa flake8 e mypy"
	@echo "  make test           Executa testes"
	@echo "  make test-watch     Executa testes em watch mode"
	@echo "  make coverage       Gera relatório de cobertura"
	@echo ""
	@echo "Outros:"
	@echo "  make pre-commit     Executa pre-commit hooks"
	@echo "  make clean          Remove arquivos gerados"
	@echo "  make docs           Gera documentação"

# ============================================================
# SETUP INICIAL
# ============================================================
setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt
	pre-commit install
	@echo "✅ Setup completo! Ative venv com: source venv/bin/activate"

install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt

# ============================================================
# FORMATAÇÃO E LINTING
# ============================================================
format:
	$(PYTHON) -m isort src/ tests/ --profile black
	$(PYTHON) -m black src/ tests/
	@echo "✅ Código formatado!"

lint:
	$(PYTHON) -m flake8 src/ tests/ --max-line-length=88
	$(PYTHON) -m mypy src/ --ignore-missing-imports
	@echo "✅ Linting completo!"

check: lint format
	@echo "✅ Verificação completa!"

# ============================================================
# TESTES
# ============================================================
test:
	$(PYTHON) -m pytest tests/ -v

test-watch:
	$(PYTHON) -m pytest tests/ -v --looponfail

test-quick:
	$(PYTHON) -m pytest tests/ -q

coverage:
	$(PYTHON) -m pytest tests/ --cov=src --cov-report=html --cov-report=term
	@echo "✅ Relatório HTML: htmlcov/index.html"

coverage-check:
	$(PYTHON) -m pytest tests/ --cov=src --cov-fail-under=80

# ============================================================
# PRE-COMMIT E QUALITY
# ============================================================
pre-commit:
	pre-commit run --all-files

pre-commit-install:
	pre-commit install

pre-commit-uninstall:
	pre-commit uninstall

security:
	$(PYTHON) -m bandit -r src/

# ============================================================
# DOCUMENTAÇÃO
# ============================================================
docs:
	@echo "Gerando documentação..."
	@echo "Nota: Implemente segundo o seu gerador (sphinx, mkdocs, etc)"

# ============================================================
# LIMPEZA
# ============================================================
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name htmlcov -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name .coverage -delete
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "✅ Limpeza completa!"

clean-all: clean
	rm -rf $(VENV)
	@echo "✅ Ambiente removido!"

# ============================================================
# DESENVOLVIMENTO LOCAL
# ============================================================
dev:
	$(PYTHON) -m uvicorn src.main:app --reload

freeze:
	$(PIP) freeze > requirements-frozen.txt

# ============================================================
# CI/CD LOCAL
# ============================================================
ci: lint coverage
	@echo "✅ CI local passou!"

# ============================================================
# DEFAULT
# ============================================================
.DEFAULT_GOAL := help
