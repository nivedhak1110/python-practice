"""
Q-1 least common multiple of two numbers in python
24=48,72,96,.....
36=36,72,108,144,....
"""
def Lcm(n1,n2):
    if n1>n2:
        higher=n1
    else:
        higher=n2
    value=higher
    while(True):
        if higher%n1==0 and higher%n2==0:
            Lcm=higher
            break
        
        else:
            higher=higher+value
    print("Lcm:",Lcm)
    
    
if __name__=='__main__':
    n1=int(input("Enter num1:"))
    n2=int(input("Enter num2:"))
    Lcm(n1,n2)
"""
Output:
Enter num1:24
Enter num2:36
Lcm: 72
******
Enter num1:12
Enter num2:20
Lcm: 60
"""
