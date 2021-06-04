"""
7.Factorial using recursion
4!=4*3*2*1=24
"""
def factorial(n,fact,i):
    if i==0:
        return fact
        
    else:
        fact=fact*i
        i=i-1
        return factorial(n,fact,i)
if __name__=='__main__':
    n=int(input("enter a number:"))
    temp=n
    fact=1
    i=n
    if(n<0):
        print("please enter a positive number")
    elif(n==0):
        print("factorial of 0 is 1")
    else:
        factorial=factorial(n,fact,i)
        print("factorial of {temp} is {factorial}".format(temp=temp,factorial=factorial))
"""
Output:
enter a number:4
factorial of 4 is 24
****
enter a number:5
factorial of 5 is 120
****
enter a number:6
factorial of 6 is 720
"""
