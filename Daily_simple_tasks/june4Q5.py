"""
5.factorial without recursion
example:
4! = 4x3x2x1 = 24  
The factorial value of 4 is 24.
The factorial value of 0 is 1 always. (Rule violation)
"""
n=int(input("enter the number:"))
temp=n
if n<0:
    print("please enter a positive number!")
elif n==0:
    print("factorial of 0 is 1")
else:
    i=n
    fact=1
    while i>0:
        fact=fact*i
        i=i-1
    print("factorial of {temp} is {fact}".format(temp=temp,fact=fact))
    
"""
output:
enter the number:3
factorial of 3 is 6
****
enter the number:4
factorial of 4 is 24

****
enter the number:-1
please enter a positive number!
****
enter the number:0
factorial of 0 is 1
"""
