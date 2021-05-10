"""
Q-15
Python Program to Print the Fibonacci sequence
Fibonacci sequence:
The Fibonacci sequence specifies a series of numbers where the 
next number is found by adding up the two numbers just before 
For example:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on"""
n=int(input("enter the number of terms required:"))

if n<0:
    print("please enter a positive number")
else:
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range(n-2):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
"""
Output:
enter the number of terms required:15
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377

"""
