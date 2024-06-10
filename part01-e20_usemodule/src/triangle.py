# Enter you module contents here
import math

__doc__ = "Module to find the hypotenuse and area"
__version__ = "1"
__author__ = "Abcdef"

def hypotenuse(a, b):
    """returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle"""
    return math.sqrt(a**2 + b**2)

def area(a, b):
    """returns the area of the right-angled triangle, when two sides, perpendicular to each other"""
    return (a*b) / 2