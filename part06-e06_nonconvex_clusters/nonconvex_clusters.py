#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN 
from sklearn.metrics import accuracy_score
import scipy
import matplotlib.pyplot as plt

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        new_label = scipy.stats.mode(real_labels[idx], keepdims=True, nan_policy='omit')[0][0]
        permutation.append(new_label)

    return permutation

def nonconvex_clusters():
    data = pd.read_csv('src/data.tsv', sep='\t')
    # X = data.loc[:, "X1":"X2"].values
    X = pd.concat([data.X1, data.X2], axis=1)
    y = data.y
    epss = np.arange(0.05, 0.2, 0.05)
    ans = []
    
    for eps in epss:
        dbscan = DBSCAN(eps=eps)
        dbscan.fit(X)
        labels = dbscan.labels_
        idx = labels != -1
        outliner = np.count_nonzero(labels == -1)

        clusters = len(set(labels)) - (1 if -1 in labels else 0)
        
        if clusters == len(y.unique()):
            permutation = find_permutation(clusters, y, labels)
            new_labels = [permutation[label] for label in labels[idx]]
            score = accuracy_score(y[idx], new_labels)
            ans.append([eps, score, clusters, outliner])
        else:
            ans.append([eps, np.NaN, clusters, outliner])

    return pd.DataFrame(ans, columns=['eps', 'Score', 'Clusters', 'Outliers'], dtype='float64')

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()