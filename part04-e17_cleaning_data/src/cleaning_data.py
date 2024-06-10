#!/usr/bin/env python3
import pandas as pd
import numpy as np

def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep='\t')

    season = {'one': 1, 'One': 1, 'two': 2, 'Two': 2}
    df['Seasons'] = df['Seasons'].replace(season).astype(int)

    df['Last'] = pd.to_numeric(df['Last'], errors='coerce', downcast='float')

    df['Start'] = df['Start'].str.split().str[0].astype(int)
    
    df['President'] = (df['President'].where(~df['President'].str.contains(','), 
                                             df['President'].str.split(',')
                                             .str[::-1]
                                             .str.join(' ')
                                             .str.strip())
                                             .str.title())

        
    df['Vice-president'] = (df['Vice-president'].where(~df['Vice-president'].str.contains(','), 
                                                       df['Vice-president'].str.split(',')
                                                       .str[::-1]
                                                       .str.join(' ')
                                                       .str.strip())
                                                       .str.title())

    df = df.astype({'President': object, 'Start': int, 'Last': float, 'Seasons': int, 'Vice-president': object})

    return df

def main():
    df = cleaning_data()
    print("dtypes:", df.dtypes)
    print(df)

if __name__ == "__main__":
    main()