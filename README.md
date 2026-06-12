# Mutual Fund Analytics Project

## Project Overview

This project analyzes Indian mutual fund data using Python, SQL, and Power BI. It includes data ingestion, cleaning, exploratory analysis, performance analysis, advanced risk metrics, and dashboard creation to generate meaningful investment insights.

## Objectives

* Perform ETL and data preprocessing.
* Analyze fund performance and NAV trends.
* Calculate risk metrics such as Sharpe Ratio, VaR, and CVaR.
* Study investor behavior and SIP continuity.
* Build a fund recommendation system.
* Create interactive Power BI dashboards.

## Datasets Used

* Fund Master Data
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Count
* Scheme Performance
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

## Technologies Used

* Python
* Pandas
* NumPy
* SQL
* SQLite
* Power BI
* Jupyter Notebook
* VS Code

## Project Structure

### Python Scripts

* data_ingestion.py
* data_cleaning.py
* database_load.py
* live_nav_fetch.py
* recommender.py
* run_pipeline.py

### Notebooks

* EDA_Analysis.ipynb
* Performance_Analytics.ipynb
* Advanced_Analytics.ipynb

### Reports

* var_cvar_report.csv
* sector_hhi_report.csv
* rolling_sharpe_chart.png

### Dashboard

* Power BI Dashboard (.pbix)

## Key Features

* Data Ingestion Pipeline
* Data Cleaning and Preprocessing
* Exploratory Data Analysis
* Performance Analytics
* Historical VaR and CVaR
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation System
* Sector HHI Concentration Analysis
* Interactive Power BI Dashboard

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the pipeline:

python run_pipeline.py

3. Execute notebooks for analysis.

4. Open the Power BI dashboard file to view visualizations.

## Future Improvements

* Live dashboard deployment.
* Machine learning-based recommendations.
* Flask web application integration.

## Author

Swarangi Kadam

Data Analyst Internship – Bluestock Fintech
