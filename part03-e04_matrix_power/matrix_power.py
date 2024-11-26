#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        size = (a.shape)[1]
        return np.eye(size)
    
    elif n < 0:
        a = np.linalg.inv(a)
        n = -n
    
    gen = (a for _ in range(n))

    return reduce(lambda x,y: x@y, gen)

def main():
    a = np.array([[1,2],
                   [3,4]])
    for n in range(-2,3):
        print(f"Power of {n}\n{matrix_power(a, n)}")

if __name__ == "__main__":
    main()