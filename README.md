# Mutual Fund Data Engineering Project

Day 1 Progress

Completed:
- Dataset ingestion and validation
- Fund master exploration
- AMFI code validation
- Data quality assessment

Pending:
- NAV API integration
- Final scripts
- Day 1 commit


Data Quality and Anomaly Observations

1. All 10 CSV files were loaded successfully using Pandas.
2. Datasets have different numbers of rows and columns based on their purpose.
3. Some datasets contain missing values in certain fields.
4. Data types include numeric, categorical, and date-related fields.
5. No corrupted files or unreadable records were observed.
6. Fund master data contains scheme-level metadata such as AMFI codes, categories, and risk classifications.
7. AMFI code validation between fund_master and nav_history was performed successfully.
8. The datasets appear suitable for further ETL processing and analysis.
