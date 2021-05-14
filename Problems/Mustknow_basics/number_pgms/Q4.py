"""
Q-4 Python program to find happy number between an interval
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
    #print(sum)
    result=sum
    return result
    
if __name__=='__main__':
    start=int(input("enter start:"))
    end=int(input("enter end:"))
    for i in range(start,end+1):
        temp=i
        result=i
        while result!=1 and result!=4:
            result=happy_number(result)
        if result==1:
            print(temp)
"""
Output:
enter start:1
enter end:100
1
7
10
13
19
23
28
31
32
44
49
68
70
79
82
86
91
94
97
100
"""
    
