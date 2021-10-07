"""
   File Name:    HW05_Alan_Clark.py
   Author:       Alan Clark
   Date:         9 Oct 2021
   Description:  Function to classify triangles, changed to follow pylint recommendations
"""

def classify_triangle(side_a: int, side_b: int, side_c: int) -> str:
    """ Function to classify a triangle by comparing its sides """
    if not (side_a > 0 and side_b > 0 and side_c > 0):
        raise ValueError('Triangle side lengths must be greater than zero, fool')
    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        raise TypeError('Triangle side lengths must be positive integers')
    result : str
    hypotenuse : int = side_a
    sum_of : int = side_b**2 + side_c**2
    # Determine the type of triangle
    if side_a == side_b:
        if side_b == side_c:
            result = "equilateral"
        else:
            result = "isoceles"
    elif side_c in (side_a, side_b):
        result = "isoceles"
    else:
        result = "scalene"
    # Now find the correct hypotenuse
    if side_b > hypotenuse:
        hypotenuse = side_b
        sum_of = side_a**2 + side_c**2
    if side_c > hypotenuse:
        hypotenuse = side_c
        sum_of = side_a**2 + side_b**2
    # So, is this a right triangle?
    if hypotenuse**2 == sum_of:
        result += ", right triangle"
    return result
