"""
Centralized configuration for the AI products monorepo.
Works from any location in the monorepo.
"""

from pathlib import Path

# Monorepo root
MONOREPO_ROOT = Path(__file__).parent.parent

# Shared directories
DATA_ROOT = MONOREPO_ROOT / "shared-assets" / "data"
MODELS_ROOT = DATA_ROOT / "models"
RAG_DB_ROOT = DATA_ROOT / "rag-databases"
LOGS_ROOT = MONOREPO_ROOT / "logs"

# AI Products
AI_PRODUCTS_ROOT = MONOREPO_ROOT / "ai-products"
SUPPLY_CHAIN_ROOT = AI_PRODUCTS_ROOT / "supply-chain-copilot"
AUTONOMOUS_AI_ROOT = AI_PRODUCTS_ROOT / "autonomous-supply-chain-ai"
ANALYTICS_ROOT = AI_PRODUCTS_ROOT / "analytics-ai-copilot"
AGENT_ASSIST_ROOT = AI_PRODUCTS_ROOT / "agent-assist-copilot"

# Create directories
for dir_path in [DATA_ROOT, MODELS_ROOT, RAG_DB_ROOT, LOGS_ROOT]:
    dir_path.mkdir(parents=True, exist_ok=True)

