#!/usr/bin/env python3
import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    m = df["Akaa":"Äänekoski"]
    five = m[(m['Share of Swedish-speakers of the population, %'] > 5) & (m['Share of foreign citizens of the population, %'] > 5)]
    return five[['Population','Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    
def main():
    df = swedish_and_foreigners()
    print("Shape: {}, {}".format(*df.shape))
    print(df)
    for i in range(3):
        print(df.iloc[i,i])

if __name__ == "__main__":
    main()