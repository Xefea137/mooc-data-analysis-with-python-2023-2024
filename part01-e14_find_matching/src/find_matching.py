#!/usr/bin/env python3
def find_matching(L, pattern):
    return [i for i, word in enumerate(L) if pattern in word]

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))   # [0, 1, 3]

if __name__ == "__main__":
    main()