#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    # return image[:,:,0] * 0.2126 + image[:,:,1] * 0.7152 + image[:,:,2] * 0.0722
    return np.dot((image[:,:,:3]), [0.2126, 0.7152, 0.0722])

def to_red(image):
    image2 = image.copy()
    image2[:,:,1:3] = 0
    # image2[:,:,[1,2]] = 0
    return image2

def to_green(image):
    image2 = image.copy()
    image2[:,:,[0,2]] = 0
    return image2

def to_blue(image):
    image2 = image.copy()
    image2[:,:,0:2] = 0
    # image2[:,:,[0,1]] = 0
    return image2

def main():
    image = plt.imread("src\\painting.png")
    plt.imshow(to_grayscale(image), cmap='gray')
    fig, ax = plt.subplots(nrows=3,ncols=1)
    ax[0].imshow(to_red(image))
    ax[1].imshow(to_green(image))
    ax[2].imshow(to_blue(image))
    plt.show()

if __name__ == "__main__":
    main()