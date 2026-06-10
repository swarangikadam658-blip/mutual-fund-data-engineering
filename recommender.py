import pandas as pd

# Load data
funds = pd.read_csv('data/processed/07_scheme_performance_clean.csv')

# Ask user for risk appetite
risk = input("Enter Risk Appetite (Low/Moderate/High): ")

# Filter matching funds
selected = funds[
    funds['risk_grade'].str.contains(
        risk,
        case=False,
        na=False
    )
]

# Sort by Sharpe ratio and take top 3
top3 = selected.sort_values(
    'sharpe_ratio',
    ascending=False
).head(3)

# Print recommendations
print("\nTop 3 Recommended Funds:\n")
print(
    top3[
        [
            'scheme_name',
            'risk_grade',
            'sharpe_ratio',
            'return_3yr_pct'
        ]
    ]
)