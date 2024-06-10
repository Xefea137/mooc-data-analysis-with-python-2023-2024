#!/usr/bin/env python3
import pandas as pd
import numpy as np

def powers_of_series(s, k):
    return pd.DataFrame({power: s**power for power in range(1,k+1)})
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()