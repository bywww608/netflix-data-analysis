"""scripts/data_cleaning.py

Simple, reusable data cleaning utilities.
Usage example:
    python scripts/data_cleaning.py --input data/raw/sample.csv --output data/cleaned/sample_cleaned.csv
"""
from pathlib import Path
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize column names
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
    # Drop exact duplicate rows
    df = df.drop_duplicates()
    # Drop columns with all nulls
    df = df.dropna(axis=1, how='all')
    # Fill numeric columns with median
    num_cols = df.select_dtypes(include=['number']).columns
    for c in num_cols:
        df[c] = df[c].fillna(df[c].median())
    # Fill object columns with empty string
    obj_cols = df.select_dtypes(include=['object', 'string']).columns
    df[obj_cols] = df[obj_cols].fillna('')
    return df

def save_clean(df: pd.DataFrame, out_path: str):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Basic CSV cleaning')
    parser.add_argument('--input', required=True, help='input csv path')
    parser.add_argument('--output', required=True, help='output csv path')
    args = parser.parse_args()
    df = load_csv(args.input)
    df = basic_clean(df)
    save_clean(df, args.output)
    print(f'Cleaned dataset saved to: {args.output}')
