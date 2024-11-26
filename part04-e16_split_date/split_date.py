#!/usr/bin/env python3
import pandas as pd
import numpy as np

def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all').dropna(axis=1, how='all')
    date = df['Päivämäärä'].str.split(expand=True)
    date.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']

    day_replace = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    date['Weekday'] = date['Weekday'].map(day_replace)

    month_replace = {'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5, 'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12}
    date['Month'] = date['Month'].map(month_replace)

    date['Hour'] = date['Hour'].str.replace(':00','')

    date = date.astype({'Weekday': object, 'Day': int, 'Month': int, 'Year': int, 'Hour': int})
    
    return date

def main():
    df = split_date()
    print("Shape:", df.shape)
    print("dtypes:", df.dtypes)
    print("Columns:", df.columns)
    print(df.head())
       
if __name__ == "__main__":
    main()
# ke 1 tammi 2014 00:00 to Wed 1 1 2014 0 