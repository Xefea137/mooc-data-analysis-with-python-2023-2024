#!/usr/bin/env python3
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def explained_variance():
    X = pd.read_csv('src/data.tsv', sep='\t')

    pca = PCA()
    pca.fit(X)
    var = X.var()
    ex_var = pca.explained_variance_

    return var, ex_var

def main():
    v, ev = explained_variance()
    print(f"The variances are: {' '.join(map(lambda x: f'{x:.3f}', v))}")
    print(f"The explained variances after PCA are: {' '.join(map(lambda x: f'{x:.3f}', ev))}")

    plt.plot(np.arange(1,11), np.cumsum(ev))
    plt.xlabel('Number of components')
    plt.ylabel('Cumulative explained variance')
    plt.title('Cumulative Explained Variance Plot')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
