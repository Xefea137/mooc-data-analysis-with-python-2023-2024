#!/usr/bin/env python3
import pandas as pd
from sklearn.linear_model import LinearRegression

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

def cycling_weather_continues(station):
    cycling = split_date_continues()
    cycling = cycling.loc[cycling['Year'] == 2017]
    
    cycling_sum = cycling.groupby(['Month', 'Day']).sum()

    weather = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    
    df = pd.merge(cycling_sum, weather, left_on=['Month', 'Day'], right_on=['m', 'd'])
    df.fillna(method='ffill', inplace=True)

    df.drop(columns=['m', 'd', 'Time', 'Time zone'], inplace=True)

    # X = df[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']].values
    X = df[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = df[station]

    model = LinearRegression()
    model.fit(X, y)
    score = model.score(X, y)
    
    return model.coef_, score
    
def main():
    coef, score = cycling_weather_continues('Baana')
    print('Measuring station: Baana')
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")

if __name__ == "__main__":
    main()