"""
Q-4
Python program to solve quadratic equation
Quadratic equation:
ax2+bx+c=0
"""
import cmath 
"""cmath module supplies equivalent functions 
on complex numbers"""
a=int(input("enter the co-efficent a: "))
b=int(input("enter the co-efficent b: "))
c=int(input("enter the co-efficent c: "))
D=(b**2)-(4*a*c)
soln1=(-b+ cmath.sqrt(D))/(2*a)
soln2=(-b- cmath.sqrt(D))/(2*a)
print("solution 1:",soln1)
print("solution 2:",soln2)
"""
Output:
enter the co-efficent a: 8
enter the co-efficent b: 16
enter the co-efficent c: 8
solution 1: (-1+0j)
solution 2: (-1+0j)
"""
