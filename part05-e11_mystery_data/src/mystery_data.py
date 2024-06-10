#!/usr/bin/env python3
import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    X = df[['X1', 'X2', 'X3', 'X4', 'X5']].values
    # X = df.loc[:, "X1":"X5"]
    y = df['Y']

    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)

    return model.coef_

def main():
    coefficients = mystery_data()
    for x in range(5):
        print(f'Coefficient of X{x+1} is {coefficients[x]}')
    
if __name__ == "__main__":
    main()