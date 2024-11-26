#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
# sns.set(color_codes=True)
sns.set_theme(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
import scipy

def toint(x):
    convert = dict(zip('ACGT', map(int, '0123')))

    return convert[x]

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    X = np.array(df['X'].map(lambda x: list(map(toint, x))).tolist())

    return X, df.y

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    # g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    g.figure.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        new_label=scipy.stats.mode(real_labels[idx], keepdims=True)[0][0]
        permutation.append(new_label)

    return permutation

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)

    clustering = AgglomerativeClustering(n_clusters=2, linkage='average', affinity='euclidean').fit(X)
    #clustering = AgglomerativeClustering(n_clusters=2, linkage='average', metric='euclidean').fit(X)

    permutation = find_permutation(2, y, clustering.labels_)
    new_labels = [permutation[label] for label in clustering.labels_]

    return accuracy_score(y, new_labels)

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)

    distance = pairwise_distances(X, metric='hamming')

    clustering = AgglomerativeClustering(n_clusters=2, linkage='average', affinity='precomputed').fit(distance)
    # clustering = AgglomerativeClustering(n_clusters=2, linkage='average', metric='precomputed').fit(distance)

    permutation = find_permutation(2, y, clustering.labels_)
    new_labels = [permutation[label] for label in clustering.labels_]
    # plot(distance, method='average', affinity='hamming')

    return accuracy_score(y, new_labels)

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()