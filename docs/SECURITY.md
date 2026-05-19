# 🔐 Política de Segurança

**Portfolio AI Products** - Guia de Segurança e Boas Práticas

---

## 📋 Índice
1. [Gestão de Credenciais](#gestão-de-credenciais)
2. [Variáveis de Ambiente](#variáveis-de-ambiente)
3. [Secrets Management](#secrets-management)
4. [Git & Versionamento](#git--versionamento)
5. [Rotação de Chaves](#rotação-de-chaves)
6. [Reportar Vulnerabilidades](#reportar-vulnerabilidades)
7. [Checklist de Segurança](#checklist-de-segurança)

---

## 🔑 Gestão de Credenciais

### ❌ NUNCA Comitar
- Chaves de API (`ANTHROPIC_API_KEY`, `GROQ_API_KEY`, etc.)
- Senhas de banco de dados
- Tokens de autenticação
- AWS/GCP/Azure credentials
- Certificados privados
- SSH keys
- Qualquer `.env` com valores reais

### ✅ O que Comitar
- Arquivos `.env.example` com valores fake/placeholder
- Templates de `.env`
- Documentação sobre quais variáveis são necessárias
- Código que lê variáveis (NÃO seus valores)

---

## 🌍 Variáveis de Ambiente

### Estrutura Obrigatória

Cada projeto deve ter:

```
project/
├── .env.example          ← Template com placeholders
├── .env                  ← Valores reais (nunca commitar)
└── .env.development     ← Dev-specific vars (nunca commitar)
```

### Criando .env.example

```bash
# Template com valores FAKE/PLACEHOLDER
ANTHROPIC_API_KEY=sk_test_...sua_chave_aqui...
GROQ_API_KEY=gsk_...sua_chave_aqui...
DATABASE_URL=postgresql://user:pass@localhost/db_test
DEBUG=False
ENVIRONMENT=development
```

### Setup Local

```bash
# 1. Clone o repositório
git clone <url>
cd portfolio-ai-products

# 2. Navegue ao projeto
cd agent-assist-copilot

# 3. Crie .env a partir do template
cp .env.example .env

# 4. Edite com suas credenciais reais
nano .env  # ou seu editor favorito

# 5. VERIFIQUE: nunca faça push de .env!
git status  # .env NÃO deve aparecer aqui
```

---

## 🗝️ Secrets Management

### Por Ambiente

#### Development
```bash
# Use chaves de teste/sandbox
# Valores podem ser compartilhados no .env.example (placeholders)
ANTHROPIC_API_KEY=sk_test_xxxxx
```

#### Staging
```bash
# Use credenciais segregadas de staging
# NUNCA reutilize staging keys em production
ANTHROPIC_API_KEY=sk_staging_xxxxx
```

#### Production
```bash
# Use variáveis de ambiente do sistema/CI/CD
# NUNCA em arquivo local
# Rotação mínimo 90 dias
ANTHROPIC_API_KEY=sk_prod_xxxxx
```

### Armazenamento Seguro

**Para Development**: `.env` local (gitignored)
**Para Staging**: CI/CD Secrets + environment variables
**Para Production**:
- AWS Secrets Manager / Systems Manager
- Google Cloud Secret Manager
- Azure Key Vault
- HashiCorp Vault

---

## 📝 Git & Versionamento

### Verificações Automáticas

Este projeto usa **pre-commit hooks** para prevenir commits acidentais:

```yaml
# .pre-commit-config.yaml inclui:
- detect-private-key    # Detecta SSH keys, credentials
- check-added-large-files  # Bloqueia arquivos >1MB
- gitleaks             # Detecta padrões de secrets
```

### Instalação de Hooks

```bash
# Instalar pre-commit hooks
pre-commit install

# Rodar manualmente em todos os arquivos
pre-commit run --all-files

# Uninstall (se necessário)
pre-commit uninstall
```

### Verificando Antes de Commitar

```bash
# Ver o que será commited
git status

# Verificar .env NÃO aparece em "Changes to be committed"
git diff --cached

# Se acidentalmente adicionou .env:
git reset HEAD .env
rm .env
```

---

## 🔄 Rotação de Chaves

### Checklist para Rotação

**Frequência**:
- ✅ Desenvolvimento: 30 dias (ou quando exposto)
- ✅ Staging: 60 dias
- ✅ Production: 90 dias (mínimo)
- 🚨 IMEDIATAMENTE: Se exposto/comprometido

### Procedimento de Rotação

#### 1. Gerar Nova Chave

```bash
# No console da API (Anthropic, Groq, etc.)
# 1. Gerar uma NOVA chave
# 2. Guardar em local seguro (password manager)
# 3. Não fazer logout ainda
```

#### 2. Atualizar Localmente

```bash
# Atualizar seu .env local
nano .env
# ANTHROPIC_API_KEY=sk_new_xxxxx
```

#### 3. Testar Nova Chave

```bash
# Rodar testes para verificar funciona
pytest
make test
```

#### 4. Atualizar em Production

```bash
# Atualizar nas CI/CD secrets / env vars
# GitHub: Settings > Secrets > Actions > Update secret
# GitLab: Settings > CI/CD > Variables
# AWS: Secrets Manager > Update secret
```

#### 5. Verificar Funcionamento

```bash
# Rodar smoke tests em staging/prod
```

#### 6. Revogar Chave Antiga

```bash
# Ir ao console da API
# Remover/desabilitar chave ANTIGA
# Confirmar: OLD_KEY is no longer valid
```

#### 7. Documentar

```bash
# Adicionar ao changelog
# Log em audit trail (who, when, why)
```

---

## 🚨 Reportar Vulnerabilidades

### Se Você Encontrou uma Vulnerabilidade

**NÃO** abra issue pública. Em vez disso:

1. **Envie email privado**:
   ```
   To: sbruno.franca@gmail.com
   Subject: [SECURITY] Portfolio AI Products Vulnerability
   Body: Descreva a vulnerabilidade
   ```

2. **Inclua**:
   - Descrição clara
   - Steps to reproduce
   - Impacto potencial
   - Sugestão de fix (se tiver)

3. **Aguarde resposta** em até 48 horas

4. **Coordene disclosure** responsável
   - Não publique antes de fix estar disponível
   - Espere nosso patch ser mergeado

### Casos de Segurança Crítica

Se encontrar credenciais expostas:

1. **Avise imediatamente**
2. **Chaves serão rotacionadas** em < 1 hora
3. **Histórico git será reescrito** para remover
4. **Force push será feito** para repo
5. **Todos devs devem fazer pull fresh**

---

## ✅ Checklist de Segurança

### Antes de Cada Commit

- [ ] Sem `.env` com valores reais
- [ ] Sem keys/tokens/credentials no código
- [ ] Sem grandes arquivos binários (> 1MB)
- [ ] Sem senhas em strings hardcoded
- [ ] Sem comentários com credenciais
- [ ] Rodei `pre-commit run --all-files`?

### Antes de Cada Push

- [ ] Verifiquei `git log` - commits fazem sentido?
- [ ] Rodei `git diff origin/main` para review final?
- [ ] Ninguém pode ver`.env` files em mudanças?
- [ ] Testes passam locally?

### Antes de Cada Deploy

- [ ] Chave NUNCA é variável de build/config pública
- [ ] Usando CI/CD secrets (não env vars públicas)
- [ ] Chave de staging é DIFERENTE de prod
- [ ] Logs não expõem credenciais parciais
- [ ] Monitoramento está ativo para abusos

### Rotina Semanal

- [ ] Verificar se há chaves antigas expostas no git
- [ ] Rever access logs de APIs
- [ ] Atualizar dependências de segurança
- [ ] Verificar pre-commit hooks estão configurados

### Rotina Mensal

- [ ] Revisar quem tem acesso a quais credenciais
- [ ] Revogar access de pessoas que saíram
- [ ] Revisar commit history de mudanças sensíveis
- [ ] Testar disaster recovery de credentials backup

---

## 🔗 Recursos Úteis

### Documentação Oficial
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Anthropic API Security](https://docs.anthropic.com/docs/api/authentication)
- [GitHub Secrets Management](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

### Ferramentas
- **gitleaks**: Detecta secrets em git history
- **detect-secrets**: Encontra patterns de secrets
- **git-filter-repo**: Remove files do histórico

### Mais Segurança

Para mais informações, veja:
- `docs/DEVELOPMENT.md` - Setup seguro local
- `.pre-commit-config.yaml` - Checks automáticos
- `docs/CONTRIBUTING.md` - Workflow seguro

---

## 📞 Suporte

**Dúvidas sobre segurança?**
- Email: sbruno.franca@gmail.com
- Slack/Discord: [@sbrunofranca](https://github.com/sbrunofranca)

**Encontrou um problema?**
- ⚠️ NÃO abra issue pública
- 📧 Envie email privado (veja acima)

---

**Última atualização**: 18 de Maio de 2026
**Status**: 🟢 Ativo e em revisão
