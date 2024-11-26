#!/usr/bin/env python3
import re

def file_listing(filename="src/listing.txt"):
    data = []
    with open (filename, "r") as f:
        for line in f:
            #data.extend(re.findall(r'(\d+)\s([A-Za-z]+)\s+(\d{,2})\s(\d{2}):(\d{2})\s([\w.]+)', line))
            data.extend(re.findall(r'(\d+)\s(...)\s+(\d+)\s(\d\d):(\d\d)\s(.+)', line))

    return [(int(a), b, int(c), int(d), int(e) ,f) for a, b, c, d, e, f in data]

def main():
    all = file_listing()
    for item in all:
        print(item)

if __name__ == "__main__":
    main()
# -rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf
# (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf")