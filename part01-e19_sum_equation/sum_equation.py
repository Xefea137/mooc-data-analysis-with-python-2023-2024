#!/usr/bin/env python3
def sum_equation(L):
    return "0 = 0" if not L else f'{" + ".join(map(str, L))} = {sum(L)}'

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()