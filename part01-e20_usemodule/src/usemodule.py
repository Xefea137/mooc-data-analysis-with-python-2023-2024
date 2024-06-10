#!/usr/bin/env python3
# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    print(triangle.hypotenuse(10, 20))
    print(triangle.area(10, 20))

if __name__ == "__main__":
    main()
