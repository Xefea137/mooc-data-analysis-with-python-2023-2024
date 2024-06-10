#!/usr/bin/env python3
import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df.replace(to_replace=["New","Re"], value=np.nan, inplace=True)
    df.dropna(how='any', inplace=True)
    return df[df['LW'].astype(int)<df['Pos']]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()