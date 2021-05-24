"""
Q-2 Greatest common divisor|Highest common factor of two numbers in python
"""
def gcd(n1,n2):
    if n1<n2:
        min=n1
    else:
        min=n2
    min_value=min
    for i in range(1,min+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    return gcd

if __name__=='__main__':
    n1=int(input("enter num1:"))
    n2=int(input("enter num2:"))
    gcd=gcd(n1,n2)
    print("GCD:",gcd)
"""
Output:
enter num1:24
enter num2:54
GCD: 6
*****
enter num1:98
enter num2:56
GCD: 14
*****
enter num1:2
enter num2:3
GCD: 1
"""
