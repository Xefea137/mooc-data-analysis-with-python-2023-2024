#!/usr/bin/env python3
import sys, math

def summary(filename):
    numbers = []
    with open (filename) as f:
        for line in f:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                continue

    total = sum(numbers)
    average = total/len(numbers)
    x = (sum([((num - average)**2) for num in numbers]))
    sd = math.sqrt(x/(len(numbers)-1))
    
    return (total, average, sd)

def main():
    for filename in sys.argv[1:]:
        data = summary(filename)
        print(f"File: {filename} Sum: {data[0]:.6f} Average: {data[1]:.6f} Stddev: {data[2]:.6f}")

    # python src/summary.py src/example.txt src/example2.txt src/example3.txt

if __name__ == "__main__":
    main()

# from statistics import stdev