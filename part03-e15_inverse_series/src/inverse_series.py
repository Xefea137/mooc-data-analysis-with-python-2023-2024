#!/usr/bin/env python3
import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, s.values)

def main():
    s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    # s = pd.Series([10, 20, 10, 40], index=['a', 'b', 'c', 'd'])
    print(inverse_series(s))

if __name__ == "__main__":
    main()

'''
What happens if some value appears multiple times in the original Series?
What happens if you use this value to index the resulting Series?
Those values will still appear at the same index
'''