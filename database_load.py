import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")

# Save to database
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

print("Database created successfully")