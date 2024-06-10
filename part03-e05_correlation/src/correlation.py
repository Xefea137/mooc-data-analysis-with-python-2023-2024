#!/usr/bin/env python3
import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    sepal_length = data[:,0]
    petal_length = data[:,2]
    correlation = scipy.stats.pearsonr(sepal_length, petal_length)

    return correlation[0]

def correlations():
    data = load()
    return np.corrcoef((data[:,0], data[:,1], data[:,2], data[:,3]))
    return np.corrcoef(data.T)
    return np.corrcoef(data[:, :4], rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()