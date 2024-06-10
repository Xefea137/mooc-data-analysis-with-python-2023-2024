#!/usr/bin/env python3
import pandas as pd

def read_series():
    index = []
    value = []
    while True:
        user_input = input("Enter index then value separated by whitespace: ")
        if user_input == "":
            return pd.Series(value, index)

        data = user_input.split()

        if len(data) != 2:
            raise Exception("Malformed input.")
        
        index.append(data[0])
        value.append(data[1])

def main():
    print(read_series())

if __name__ == "__main__":
    main()