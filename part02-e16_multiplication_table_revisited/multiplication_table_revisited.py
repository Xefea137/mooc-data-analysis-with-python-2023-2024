#!/usr/bin/env python3
import numpy as np

def multiplication_table(n):
    row = np.arange(n)
    col = row.reshape(n,1)
    # print(np.broadcast_arrays(row,col))
    return row*col
    return row[:, np.newaxis] * row[np.newaxis, :]

def main():
    print(multiplication_table(11))

if __name__ == "__main__":
    main()