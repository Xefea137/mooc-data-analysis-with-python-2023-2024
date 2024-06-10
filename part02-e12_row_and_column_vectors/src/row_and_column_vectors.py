#!/usr/bin/env python3
import numpy as np

def get_row_vectors(a):
    # return [row.reshape(1, a.shape[1]) for row in a]
    return np.split(a, a.shape[0], axis=0)

def get_column_vectors(a):
    # return [row.reshape(a.shape[0], 1) for row in a.T]
    return np.split(a, a.shape[1], axis=1)

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    # a=np.array([[5,0,3], [3,7,9]])
    print("a:\n", a)
    print("Row vectors:\n", get_row_vectors(a))
    print("Column vectors:\n", get_column_vectors(a))

if __name__ == "__main__":
    main()