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

def bicycle_timeseries():
    data = split_date_continues()

    data['Date'] = pd.to_datetime(data[['Year', 'Month', 'Day', 'Hour']])
    data.set_index('Date', inplace=True)

    data.drop(columns=['Day', 'Month', 'Year', 'Hour'], inplace=True)

    return data

def commute():
    data = bicycle_timeseries()

    aug_17 = data.loc['2017-08']
    # aug_17 = data["2017-8-1":"2017-8-31"]

    weekday_group = aug_17.groupby('Weekday').sum()

    weekday_replace = dict(zip('Mon Tue Wed Thu Fri Sat Sun'.split(), range(1,8)))
    weekday_group.index = weekday_group.index.map(weekday_replace)
    weekday_group.sort_index(inplace=True)

    return weekday_group
    
def main():
    data = commute()
    plt.plot(data)
    weekdays="x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()

if __name__ == "__main__":
    main()