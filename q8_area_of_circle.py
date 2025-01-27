# 8) Python program to calculate the area of a circle

#import math module for constant pi
import math

# input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# calculate the area of the circle
area = math.pi * (radius ** 2)

# print the result
print(f"The area of the circle with radius {radius} is: {area:.2f}.")