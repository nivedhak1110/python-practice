""" Q-3 Python program to find the area of a triangle
Mathematical formula:
Heron's formula
Area of a triangle = (s*(s-a)*(s-b)*(s-c))**0.5(sqrt)
a,b,c are the sidews of the triangle
Here s is the semi-perimeter and a, b and c are three sides of
the triangle."""
a=int(input("enter the side a:"))
b=int(input("enter the side b:"))
c=int(input("enter the side c:"))
#semiperimeter
s=(a+b+c)/2
print("semiperimeter:",s)
#area of the triangle
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area of the triangle: %0.2f"%area)
"""
Output:
enter the side a:20
enter the side b:20
enter the side c:10
semiperimeter: 25.0
area of the triangle: 96.82

"""
