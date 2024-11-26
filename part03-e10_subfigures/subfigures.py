#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1, 2, figsize=(8,5))

    plt.suptitle("Subfigures")

    ax[0].plot(a[:,0],a[:,1])
    ax[0].set_title("plot()")
    ax[0].set_xlabel("X-axis")
    ax[0].set_ylabel("Y-axis")

    ax[1].scatter(a[:,0],a[:,1],c=a[:,2],s=a[:,3])
    ax[1].set_title("scatter()")
    ax[1].set_xlabel("X-axis")
    ax[1].set_ylabel("Y-axis")

    plt.show()

def main():
    n = 10
    a = np.random.randint(0, 10, (n, 3))
    print(a)
    print(a.dtype)
    print(a.shape)
    a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)
    print(a)
    subfigures(a)

if __name__ == "__main__":
    main()