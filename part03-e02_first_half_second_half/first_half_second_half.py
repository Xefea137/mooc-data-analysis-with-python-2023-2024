#!/usr/bin/env python3
import numpy as np

def first_half_second_half(a):
    left, right = np.split(a, 2, axis=1)

    result = np.sum(left,axis=1) > np.sum(right,axis=1)

    return a[result]
    return a[np.sum(a[:,:m],axis=1) > np.sum(a[:,m:],axis=1)]

def main():
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()