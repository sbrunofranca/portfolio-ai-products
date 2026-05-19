# 🤝 Guia de Contribuição

Obrigado por se interessar em contribuir para o Portfolio AI Products! Este documento fornece orientações para participar do projeto.

---

## 📋 Índice

1. [Código de Conduta](#código-de-conduta)
2. [Como Começar](#como-começar)
3. [Processo de Desenvolvimento](#processo-de-desenvolvimento)
4. [Padrões de Código](#padrões-de-código)
5. [Testes](#testes)
6. [Commits e Pull Requests](#commits-e-pull-requests)
7. [Dúvidas?](#dúvidas)

---

## 📜 Código de Conduta

### Nossos Compromissos

Nos comprometemos em fornecer um ambiente acolhedor e inclusivo para todos. Todos devem:

- Ser respeitosos com opiniões diferentes
- Aceitar críticas construtivas
- Focar no que é melhor para a comunidade
- Mostrar empatia com outros membros

### Exemplos Inaceitáveis

- Linguagem ou imagens sexualizadas
- Bullying, insultos ou ataques pessoais
- Assédio público ou privado
- Doxxing ou compartilhamento de informações privadas
- Discriminação de qualquer tipo

**Violações podem resultar em exclusão do projeto.**

---

## 🚀 Como Começar

### 1. **Prepare seu Ambiente**

```bash
# Clone o repositório
git clone https://github.com/sbrunofranca/portfolio-ai-products.git
cd portfolio-ai-products

# Escolha o projeto
cd agent-assist-copilot

# Crie um virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. **Crie uma Branch**

```bash
# Atualize main
git checkout main
git pull origin main

# Crie sua branch com padrão descritivo
git checkout -b feature/sua-feature
# ou
git checkout -b bugfix/seu-bug
git checkout -b docs/sua-documentacao
```

### 3. **Faça suas Mudanças**

Siga os padrões de código (ver seção abaixo).

### 4. **Teste Localmente**

```bash
# Execute testes
pytest

# Com cobertura
pytest --cov=src tests/

# Verify code quality
flake8 src/ tests/
black --check src/ tests/
mypy src/
```

### 5. **Envie seu Trabalho**

```bash
# Commit com mensagem descritiva
git commit -m "feat(auth): adiciona autenticação OAuth"

# Push para sua fork
git push origin feature/sua-feature

# Abra Pull Request no GitHub
```

---

## 🔄 Processo de Desenvolvimento

### Git Workflow

```
main (branch principal, sempre estável)
  ↑
  ├── feature/nova-funcionalidade
  ├── bugfix/correcao-bug
  ├── docs/atualizacao-docs
  └── refactor/melhoria-codigo
```

### Branch Naming Convention

| Tipo | Exemplo | Descrição |
|------|---------|-----------|
| Feature | `feature/oauth-integration` | Nova funcionalidade |
| Bug Fix | `bugfix/login-error` | Correção de bug |
| Hotfix | `hotfix/critical-security` | Correção crítica |
| Documentation | `docs/api-guide` | Documentação |
| Refactor | `refactor/async-support` | Reorganização de código |
| Performance | `perf/cache-optimization` | Otimização de performance |
| Tests | `test/add-integration-tests` | Testes |

### Pull Request Checklist

Antes de enviar um PR, certifique-se de:

- [ ] Branch atualizado com `main`
- [ ] Todos os testes passam (`pytest`)
- [ ] Código segue padrões de formatação (`black`, `flake8`)
- [ ] Types estão corretos (`mypy`)
- [ ] Cobertura de testes adequada (>80%)
- [ ] Documentação atualizada (docstrings, README se necessário)
- [ ] Sem conflitos de merge
- [ ] Commits com mensagens claras

---

## 📝 Padrões de Código

### Python Style Guide

Seguimos **PEP 8** com exceções do `black`:

```python
# ✅ BOM: Nomes descritivos, tipos, docstrings
def calculate_discount(price: float, percentage: float) -> float:
    """
    Calcula desconto baseado em percentual.

    Args:
        price: Preço original em reais
        percentage: Percentual de desconto (0-100)

    Returns:
        Preço com desconto aplicado

    Raises:
        ValueError: Se percentage não está entre 0-100
    """
    if not 0 <= percentage <= 100:
        raise ValueError(f"Percentual inválido: {percentage}")

    return price * (1 - percentage / 100)


# ❌ RUIM: Nomes genéricos, sem tipos
def calc(p, pct):
    return p * (1 - pct / 100)
```

### Principais Regras

1. **Type Hints Obrigatórios**
   ```python
   def process_data(items: list[str]) -> dict[str, int]:
       ...
   ```

2. **Docstrings em Funções Públicas**
   ```python
   def public_function(param: str) -> bool:
       """Descrição breve.

       Descrição mais detalhada se necessário.

       Args:
           param: Descrição do parâmetro

       Returns:
           Descrição do retorno
       """
   ```

3. **Máximo 88 caracteres por linha** (padrão `black`)

4. **Imports organizados**
   ```python
   # Stdlib
   import os
   from pathlib import Path

   # Third-party
   import fastapi
   from anthropic import Anthropic

   # Local
   from .models import User
   from .utils import helper
   ```

5. **Use context managers** para recursos
   ```python
   # ✅ BOM
   with open(file) as f:
       data = f.read()

   # ❌ RUIM
   f = open(file)
   data = f.read()
   f.close()
   ```

### Estrutura de Projeto

```
src/projeto/
├── __init__.py
├── main.py              # Ponto de entrada
├── config.py            # Configurações
├── models.py            # Modelos de dados
├── services/            # Lógica de negócio
│   ├── __init__.py
│   ├── user_service.py
│   └── auth_service.py
├── routes/              # Endpoints (FastAPI)
│   ├── __init__.py
│   ├── users.py
│   └── auth.py
└── utils/               # Funções auxiliares
    ├── __init__.py
    ├── decorators.py
    └── helpers.py
```

---

## 🧪 Testes

### Requisitos

- Mínimo 80% de cobertura
- Cada feature nova requer testes
- Bugfixes devem incluir teste que falha antes da fix

### Estrutura de Testes

```python
# tests/test_models.py
import pytest
from src.projeto.models import User


class TestUser:
    """Testes para modelo User."""

    def test_user_creation(self):
        """Deve criar usuário com sucesso."""
        user = User(name="João", email="joao@example.com")
        assert user.name == "João"
        assert user.email == "joao@example.com"

    def test_user_invalid_email(self):
        """Deve rejeitar email inválido."""
        with pytest.raises(ValueError):
            User(name="João", email="invalid-email")

    @pytest.mark.asyncio
    async def test_user_save_async(self):
        """Deve salvar usuário assincronamente."""
        user = User(name="João", email="joao@example.com")
        result = await user.save()
        assert result.id is not None
```

### Executar Testes

```bash
# Todos os testes
pytest

# Específico
pytest tests/test_models.py

# Com padrão
pytest -k "test_user"

# Com cobertura
pytest --cov=src tests/

# Report HTML
pytest --cov=src --cov-report=html tests/
```

---

## 💬 Commits e Pull Requests

### Mensagens de Commit

Seguimos **Conventional Commits**:

```
<tipo>(<escopo>): <descrição breve>

<corpo (opcional)>

<footer (opcional)>
```

#### Tipos

- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Documentação
- **style**: Formatação, sem mudança de lógica
- **refactor**: Reorganização de código
- **perf**: Otimização de performance
- **test**: Adição/modificação de testes
- **chore**: Dependências, configuração

#### Exemplos

```
feat(auth): adiciona autenticação OAuth 2.0

Implementa fluxo de autenticação usando Google OAuth.
Inclui validação de token e refresh automático.

Fixes #123
```

```
fix(api): corrige erro 500 em POST /users

O endpoint retornava erro quando email duplicado.
Adicionado validação prévia e mensagem de erro clara.

Fixes #456
```

```
docs(readme): atualiza instruções de setup

Clarifica versão mínima de Python e dependências opcionais.
```

### Pull Request

**Título**: Use o mesmo padrão de commit
```
feat(api): adiciona endpoint de relatórios
```

**Descrição**:
```markdown
## 📝 Descrição

Breve descrição do que foi feito e por quê.

## 🔗 Issue Relacionada

Fixes #123

## 🧪 Testes

- [ ] Testes unitários adicionados
- [ ] Testes de integração adicionados
- [ ] Cobertura > 80%

## 📸 Screenshots (se aplicável)

[Adicione screenshots ou GIFs]

## ✅ Checklist

- [x] Código segue padrões do projeto
- [x] Autotestes adicionados
- [x] Documentação atualizada
- [x] Sem breaking changes (ou explicado)
```

### Code Review

Esperamos que:
- Mantenha tom respeitoso e construtivo
- Responda a todas as sugestões
- Faça ajustes solicitados em novos commits
- Não force-push em PRs sob review (a menos que solicitado)

---

## 🎯 Checklist para Contribuidor

- [ ] Li o README e entendo o projeto
- [ ] Configurei ambiente de desenvolvimento
- [ ] Criei branch com nome descritivo
- [ ] Implementei a funcionalidade/fix
- [ ] Adicionei testes
- [ ] Executei `pytest`, `black`, `flake8`, `mypy`
- [ ] Atualizei documentação
- [ ] Criei commit(s) com mensagens claras
- [ ] Abri PR com descrição detalhada
- [ ] Respondi a comentários de review

---

## 🆘 Dúvidas?

### Recursos

- **Documentação**: [docs/](./docs/)
- **Issues**: [Discussões abertas](../../issues)
- **Discussions**: [Q&A](../../discussions)
- **Email**: sbruno.franca@gmail.com

### Tipos de Contribuição Bem-Vindos

- 🐛 Reportar bugs
- ✨ Sugerir features
- 📚 Melhorar documentação
- 🧪 Adicionar testes
- ⚡ Otimizar código
- 🔐 Reportar vulnerabilidades (responsavelmente)

### Security Issues

⚠️ **NÃO** abra uma issue pública para vulnerabilidades!

Envie email para: sbruno.franca@gmail.com com detalhes.

---

## 📊 Estatísticas do Projeto

- **Python**: 89.6%
- **C++**: 6.7%
- **C**: 0.8%
- **Fortran**: 0.1%
- **JavaScript**: 0.0%

---

**Obrigado por contribuir! 🎉**

Suas contribuições fazem este projeto melhor para todos.

---

*Última atualização: 18 de Maio de 2026*
