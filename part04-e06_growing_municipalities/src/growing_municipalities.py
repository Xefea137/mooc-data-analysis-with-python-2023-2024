#!/usr/bin/env python3
import pandas as pd

def growing_municipalities(df):
    return df[df['Population change from the previous year, %'] > 0].shape[0] / df['Population change from the previous year, %'].shape[0]

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    df = df["Akaa":"Äänekoski"]
    print(f'Proportion of growing municipalities: {(growing_municipalities(df)*100):.1f}%')

if __name__ == "__main__":
    main()