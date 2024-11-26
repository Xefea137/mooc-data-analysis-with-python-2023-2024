#!/usr/bin/env python3
def main():
    for c in range(1, 11):
        for r in range(1, 11):
            print(f"{c*r:4d}", end="")
        print()

if __name__ == "__main__":
    main()