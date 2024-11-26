#!/usr/bin/env python3
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression()
    model.fit(x[:, np.newaxis], y)
    return model.coef_[0], model.intercept_
    
def main():
    np.random.seed(0)
    n = 20
    x = np.linspace(0, 10, n)
    y = x*2 + 1 + 1*np.random.randn(n)
    slope, intercept = fit_line(x, y)
    print(f"Slope: {slope}")
    print(f'Intercept: {intercept}')

    plt.scatter(x, y)
    x1 = np.linspace(min(x)-1, max(x)+1, 10)
    plt.plot(x1, x1*slope + intercept, 'red')

    plt.show()
    
if __name__ == "__main__":
    main()