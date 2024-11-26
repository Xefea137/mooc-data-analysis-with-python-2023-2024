#!/usr/bin/env python3
import math

def triangle(base, height):
    return base * height / 2

def rectangle(width, height):
    return width * height

def circle(radius):
    return math.pi * radius ** 2

def main():
    # enter you solution here
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        
        if shape not in ("triangle", "rectangle", "circle"):
            print("Unknown shape!")

        if shape == "triangle":
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            print(f"The area is {triangle(base, height):.6f}")

        if shape == "rectangle":
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            print(f"The area is {rectangle(width, height):.6f}")

        if shape == "circle":
            radius = int(input("Give radius of the circle: "))
            print(f"The area is {circle(radius):.6f}")

if __name__ == "__main__":
    main()