"""
Q-3 Python program to check if the given number is Happy Number
+++++
Happy Number:
A number is called happy if it leads to 1 after a sequence 
of steps wherein each step number is replaced by the sum of 
squares of its digit that is if we start with Happy Number
and keep replacing it with digits square sum, we reach 1. 
+++++
Input: n = 19
Output: True
19 is Happy Number,
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
As we reached to 1, 19 is a Happy Number.
"""
def happy_number(num):
    
    sum=0
    while num>0:
        rem=num%10
        sum=sum+(rem**2)
        num=num//10
    print(sum)
    result=sum
    return result
    
if __name__=='__main__':
    num=int(input("enter a number:"))
    result=num
    while result!=1 and result!=4:
        result=happy_number(result)
    if result==1:
        print("Happy number")
        
    elif result==4:
        print("Unhappy number")
"""
Output:
enter a number:446
#68
#100
#1
Happy number
*****
enter a number:445
Unhappy number
"""
