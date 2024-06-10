#!/usr/bin/env python3
import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df = df[(df['LW'] != 'New') & (df['LW'] != 'Re')]
    df['LW'] = df['LW'].astype(int)
    df['Peak Pos'] = np.where((df['Peak Pos'] == df['Pos']) & (df['Pos'] < df['LW']), np.nan, df['Peak Pos'])
    df.sort_values(by='LW', inplace=True)
    df.index = df['LW']
    df = df.reindex(range(1,41))
    df['LW'] = np.nan
    df['Pos'] = df.index
    df.WoC -= 1

    return df

def main():
    # print(last_week())
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)

if __name__ == "__main__":
    main()