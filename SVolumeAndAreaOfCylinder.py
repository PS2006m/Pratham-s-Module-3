'''
Write a Python program to calculate surface volume and area of a
cylinder
'''
import math
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = math.pi * radius**2 * height
area = 2 * math.pi * radius * (radius + height)
print("Surface colume is ",volume)
print("Area is ",area)
