"""scripts/visualization.py

Reusable plotting helpers. Saves plots into the charts/ folder by default.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

def plot_time_series(df, date_col, value_col, out_path, title=None, figsize=(10,5)):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.sort_values(date_col)
    plt.figure(figsize=figsize)
    plt.plot(df[date_col], df[value_col], marker='o')
    plt.xlabel(date_col)
    plt.ylabel(value_col)
    if title: plt.title(title)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def bar_by_group(df, group_col, value_col, out_path, title=None, figsize=(10,6)):
    agg = df.groupby(group_col)[value_col].sum().sort_values(ascending=False)
    plt.figure(figsize=figsize)
    sns.barplot(x=agg.values, y=agg.index)
    if title: plt.title(title)
    plt.xlabel(value_col)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

if __name__ == '__main__':
    print('This module provides plot_time_series and bar_by_group helpers.')
