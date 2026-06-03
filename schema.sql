CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date DATE
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount REAL,
    transaction_date DATE
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL
);

CREATE TABLE fact_aum (
    amfi_code INTEGER,
    aum REAL
);