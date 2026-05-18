from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/sample.db")

with engine.connect() as conn:

    # =========================================================
    # CRIA TABELA SALES
    # =========================================================
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        revenue REAL
    )
    """))

    # =========================================================
    # INSERE DADOS MOCK
    # =========================================================
    conn.execute(text("""
    INSERT INTO sales (date, revenue) VALUES
    ('2026-04-01', 1000),
    ('2026-04-15', 1500),
    ('2026-04-28', 2000),
    ('2026-05-01', 3000),
    ('2026-05-10', 2500),
    ('2026-05-17', 1800)
    """))

    conn.commit()

print("Banco inicializado com sucesso!")