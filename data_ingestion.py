import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

for file in csv_files:
    file_path = os.path.join(DATA_PATH, file)

    print("=" * 60)
    print("FILE:", file)

    df = pd.read_csv(file_path)

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")