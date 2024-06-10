#!/usr/bin/env python3

def triple(num: int):
    "Multiplies its parameter by three"
    return num * 3

def square(num: int):
    "Raises its parameter to the power of two"
    return num ** 2

def main():
    for num in range(1, 11):
        triple_result = triple(num)
        square_result = square(num)
        if square_result > triple_result:
            break
        print(f"triple({num})=={triple_result} square({num})=={square_result}")

if __name__ == "__main__":
    main()