# Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|---------|-------------|
| amfi_code | Integer | Unique AMFI fund code |
| fund_name | Text | Fund scheme name |
| fund_house | Text | AMC name |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |

## 02_nav_history.csv

| Column | Type | Description |
|----------|---------|-------------|
| amfi_code | Integer |
| date | Date |
| nav | Float |

## 07_scheme_performance.csv

| Column | Type | Description |
|----------|---------|-------------|
| return_1y | Float |
| return_3y | Float |
| return_5y | Float |
| expense_ratio | Float |

## 08_investor_transactions.csv

| Column | Type | Description |
|----------|---------|-------------|
| transaction_type | Text |
| amount | Float |
| transaction_date | Date |