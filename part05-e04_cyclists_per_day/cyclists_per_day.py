#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

def split_date(df):
    date = df['Päivämäärä'].str.split(expand=True)
    date.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']

    day_replace = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
    date['Weekday'] = date['Weekday'].map(day_replace)

    month_replace = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))
    date['Month'] = date['Month'].map(month_replace)

    date['Hour'] = date['Hour'].str.replace(':00','')

    date = date.astype({'Weekday': object, 'Day': int, 'Month': int, 'Year': int, 'Hour': int})
    return date

def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all').dropna(axis=1, how='all')

    date = split_date(df)

    df.drop(columns='Päivämäärä', inplace=True)
    
    return pd.concat([date, df], axis=1)

def cyclists_per_day():
    df = split_date_continues()
    df.drop(columns=['Weekday', 'Hour'], inplace=True)
    groups = df.groupby(['Year', 'Month', 'Day']).sum()

    return groups
    
def main():
    df = cyclists_per_day()
    print("Shape:", df.shape)
    print("Columns types:", df.dtypes)
    df = df.loc[(2017, 8), :]
    df.plot()
    plt.show()

if __name__ == "__main__":
    main()