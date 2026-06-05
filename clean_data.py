import pandas as pd

# clean 02_nav_history

nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)
print(nav.head())

# convert date

nav['date'] = pd.to_datetime(nav['date'])
print(nav.dtypes)

# sort the values

nav = nav.sort_values(
    ['amfi_code','date']
)

# remove duplicates

nav = nav.drop_duplicates()

# check invalid values

invalid_nav = nav[
    nav['nav'] <= 0
]

print(len(invalid_nav))


nav['nav'] = nav.groupby(
    'amfi_code'
)['nav'].ffill()

# save through

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

# clean data \ 08_invester_transactions

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# check values
print(
    txn['transaction_type'].unique()
)

# converted values
txn['transaction_type'] = (
    txn['transaction_type']
    .str.strip()
    .str.title()
)

# find invalid amounts

txn[
    txn['amount_inr'] <= 0
]

txn = txn[
    txn['amount_inr'] > 0
]

# convert date

txn['transaction_date'] = pd.to_datetime(
    txn['transaction_date']
)

# validate kyc

print(
    txn['kyc_status'].unique()
)

valid = [
    'Verified',
    'Pending'
]

bad = txn[
    ~txn['kyc_status'].isin(valid)
]

print(len(bad))

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

# clean 07 scheme_performance.csv

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

#validate numeric returns

cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct'
]

for col in cols:

    perf[col] = pd.to_numeric(
        perf[col],
        errors='coerce'
    )

# check missing
print(
    perf[cols].isnull().sum()
)

#find anamolies
anomalies = perf[
    (perf['expense_ratio_pct'] < 0.1)
    |
    (perf['expense_ratio_pct'] > 2.5)
]

print(anomalies)

# save through
perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

