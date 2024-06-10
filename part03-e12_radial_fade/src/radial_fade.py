#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def center(a):
    y = (a.shape[0]-1)/2
    x = (a.shape[1]-1)/2
    return (y, x)  # note the order: (center_y, center_x)

def radial_distance(a):
    c = center(a)
    result = []
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            e_distance = np.linalg.norm((j-c[1], i-c[0]))
            result.append(e_distance)

    e_distance = np.array(result).reshape((a.shape[0], a.shape[1]))

    return e_distance

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range [tmin,tmax]."""
    return np.interp(a, (np.min(a), np.max(a)), (tmin, tmax))

def radial_mask(a):
    return scale(1-radial_distance(a))

def radial_fade(a):
    return a*radial_mask(a)[:,:,np.newaxis]

def main():
    image = plt.imread("src//painting.png")
    fig, ax = plt.subplots(3,1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()

if __name__ == "__main__":
    main()