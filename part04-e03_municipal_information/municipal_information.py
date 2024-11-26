#!/usr/bin/env python3
import pandas as pd

def main():
    df = pd.read_csv('src/municipal.tsv', delimiter='\t')
    r, c = df.shape
    print(f"Shape: {r},{c}")
    print("Columns:")
    for item in df.columns:
        print(item)

if __name__ == "__main__":
    main()