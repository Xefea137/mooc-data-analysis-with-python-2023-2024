#!/usr/bin/env python3
import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    multiply = np.multiply(X,Y)
    sum = np.sum(multiply, axis=1)

    X_mag = np.linalg.norm(X, axis=1)
    Y_mag = np.linalg.norm(Y, axis=1)

    angle = np.arccos(np.round(sum/(X_mag*Y_mag)))

    degree = angle*(180/np.pi)

    return degree

def main():
    np.array([])
    A=np.array([[0,0,1], [-1,1,0]])
    B=np.array([[0,1,0], [1,1,0]])
    result = vector_angles(A,B)
    print(result)

if __name__ == "__main__":
    main()