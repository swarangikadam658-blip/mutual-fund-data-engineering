import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# -------------------------------
# 1. Clean NAV History
# -------------------------------
nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

if "nav" in nav.columns:
    nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV History cleaned")

# -------------------------------
# 2. Clean Investor Transactions
# -------------------------------
transactions = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

transactions = transactions.drop_duplicates()

if "amount" in transactions.columns:
    transactions = transactions[
        transactions["amount"] > 0
    ]

transactions.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions cleaned")

# -------------------------------
# 3. Clean Scheme Performance
# -------------------------------
performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

performance = performance.drop_duplicates()

performance.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance cleaned")

print("All cleaning completed successfully")