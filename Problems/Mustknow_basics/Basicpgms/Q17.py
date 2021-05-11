"""
Q-17
Python Program to Find Armstrong Number between an Interval
"""
start=int(input("enter start of the interval: "))
end=int(input("enter end of the interval: "))
for i in range(start,end+1):
    temp=i
    count=0
    while i>0:
        i=i//10
        count=count+1
    num=temp
    sum=0
    while num>0:
        rem=num%10
        sum=sum+(rem**count)
        num=num//10
    if temp==sum:
        print(temp)
"""
Output:
****
enter start of the interval: 1
enter end of the interval: 1000
1
2
3
4
5
6
7
8
9
153
370
371
407
****
enter start of the interval: 500
enter end of the interval: 10000
1634
8208
9474
******
"""
