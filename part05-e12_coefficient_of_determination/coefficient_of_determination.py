#!/usr/bin/env python3
import pandas as pd
from sklearn import linear_model

def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    X = df.loc[:, 'X1':'X5']
    y = df['Y']

    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(X, y)
    r2 = model.score(X, y)
    result = [r2]
    
    for column in df.columns:
        r = df[[column]]
        model.fit(r, y)
        c = model.score(r, y)
        result.append(c)
        
    return result
    
def main():
    a = coefficient_of_determination()
    print(f'R2-score with feature(s) X: {a[0]}')
    for x in range(1, 6):
        print(f'R2-score with feature(s) X{x}: {a[x]:.2f}')
        
if __name__ == "__main__":
    main()