"""
Q-18
Python Program to Find the Sum of n Natural Numbers
Natural numbers:
As the name specifies, a natural number is the number that 
occurs commonly and obviously in the nature. It is a whole,
non-negative number.
N= {1, 2, 3, 4, .... and so on}  
"""
n=int(input("enter n:"))
if n<1:
    print("please enter a positive number")
else:
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print("sum of first {n} natural numbers is {sum}".format(n=n,sum=sum))
"""
Output:
enter n:10
sum of first 10 natural numbers is 55
enter n:100
sum of first 100 natural numbers is 5050
"""
