"""
Python Program to Find the Factorial of a Number
What is factorial?
Factorial is a non-negative integer. It is the product of all 
positive integers less than or equal to that number for which 
you ask for factorial. It is denoted by exclamation sign (!).

For example:
4! = 4x3x2x1 = 24  
The factorial value of 4 is 24.

Note: The factorial value of 0 is 1 always. (Rule violation)
"""

num=int(input("enter a number:"))
if num<0:
    print("factorial doesnot exist for negative numbers")
elif num==0:
    print("factorial of 0 is 1")
else:
    i=num
    fact=1
    while i>0:
        fact=fact*i
        i=i-1
    print("factorial of {num} is {fact}".format(num=num,fact=fact))
"""
Output:
enter a number:4
factorial of 4 is 24
enter a number:3
factorial of 3 is 6

enter a number:-2
factorial doesnot exist for negative numbers

enter a number:0
factorial of 0 is 1

"""
