#!/usr/bin/env python3
import pandas as pd

def average_temperature():
    df = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    return df[df['m']==7].describe().loc['mean', 'Air temperature (degC)']
    
    df_J = df[df['m']==7]
    return df_J['Air temperature (degC)'].mean()

def main():
    print(f'Average temperature in July: {average_temperature()}')

if __name__ == "__main__":
    main()