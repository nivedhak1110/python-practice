"""
Q11
Python Program to Check Prime Number
Prime numbers:

A prime number is a natural number greater than 1 and havingno
positive divisor other than 1 and itself.
For example: 3, 7, 11 ... are prime numbers.
"""
num=int(input("enter a number: "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("Prime number")
else:
    print("Not a prime number")
"""
Output:
enter a number: 2
Prime number
enter a number: 4
Not a prime number
"""
    
