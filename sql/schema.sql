CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    sub_category TEXT
);

CREATE TABLE dim_date (

    date_key INTEGER PRIMARY KEY,

    full_date DATE,

    year INTEGER,

    month INTEGER,

    quarter INTEGER
);

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY,

    amfi_code INTEGER,

    date_key INTEGER,

    nav REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY(date_key)
        REFERENCES dim_date(date_key)
);

CREATE TABLE fact_transactions (

    transaction_id INTEGER PRIMARY KEY,

    amfi_code INTEGER,

    date_key INTEGER,

    amount_inr REAL,

    transaction_type TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (

    perf_id INTEGER PRIMARY KEY,

    amfi_code INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (

    aum_id INTEGER PRIMARY KEY,

    fund_house TEXT,

    aum_crore REAL
);

SELECT COUNT(*)
FROM dim_fund;