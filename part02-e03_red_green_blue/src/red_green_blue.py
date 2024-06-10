#!/usr/bin/env python3
import re

def red_green_blue(filename="src/rgb.txt"):
    data = []
    with open (filename) as f:
        for line in f:
            data.extend(re.findall(r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)', line))

    return ["\t".join(item) for item in data]

def main():
    result = red_green_blue()
    for item in result:
        print(item)

if __name__ == "__main__":
    main()
    #255 250 250		snow
    #'255\t250\t250\tsnow'