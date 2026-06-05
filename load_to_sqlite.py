import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# load CSVs into SQLite

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists='replace',
    index=False
)

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

txn = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

perf = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)
print("Database loaded sucessfully!")

#load all data sets

nav.to_sql(...)
txn.to_sql(...)
perf.to_sql(...)

print(len(fund_master))
print(len(nav))
print(len(txn))