#!/usr/bin/env python3
import numpy as np

def diamond(n):
    top_right = np.eye(n, dtype=int)
    top_left = top_right[:,::-1]

    top = np.concatenate((top_left[:,:n-1], top_right), axis=1)
    # top = np.concatenate((top_left, top_right[:,1:]), axis=1)

    bottom = top[::-1,:]

    result = np.concatenate((top, bottom[1:,:]))
    # result = np.concatenate((top[:-1,:], bottom))
    
    return result

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()