# 📜 Scripts - Utilitários do Projeto

Diretório contendo scripts de automação, setup e manutenção para o projeto **Portfolio AI Products**.

## 📁 Estrutura

```
scripts/
├── README.md                      # Este arquivo
├── setup/                         # Scripts de configuração inicial
│   ├── complete-setup.py          # Setup completo do projeto
│   └── apply-to-all-projects.py   # Aplicar mudanças em todos os projetos
├── maintenance/                   # Scripts de manutenção
│   ├── clean-external-tests.py    # Limpar testes externos
│   ├── reorganize-tests.py        # Reorganizar estrutura de testes
│   └── fix-tests.sh               # Corrigir issues de testes
└── utils/                         # Utilitários gerais
    └── apply-changes.py           # Aplicar mudanças específicas
```

## 🚀 Como Usar

### Setup Inicial

```bash
# Setup completo (venv, deps, pre-commit hooks)
python scripts/setup/complete-setup.py

# Ou manualmente:
cd <project>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
```

### Aplicar Mudanças em Todos os Projetos

```bash
# Aplicar uma mudança em todos os projetos
python scripts/setup/apply-to-all-projects.py
```

### Manutenção

```bash
# Limpar testes externos
python scripts/maintenance/clean-external-tests.py

# Reorganizar estrutura de testes
python scripts/maintenance/reorganize-tests.py

# Corrigir issues de testes
bash scripts/maintenance/fix-tests.sh
```

### Aplicar Mudanças Específicas

```bash
# Ferramenta genérica para aplicar mudanças
python scripts/utils/apply-changes.py
```

## ⚠️ Nota Importante

Estes scripts foram criados para automação específica do projeto. Revise o código antes de executar em produção.

## 📝 Documentação

Para mais informações sobre setup e desenvolvimento, veja:
- [DEVELOPMENT.md](../docs/DEVELOPMENT.md)
- [CONTRIBUTING.md](../docs/CONTRIBUTING.md)

---

**Última atualização**: 18 de Maio de 2026
