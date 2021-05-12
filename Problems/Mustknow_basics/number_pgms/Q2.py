"""
Q-2
Python program to print all disarium numbers between 1 and 
1000
For example, 175 is a Disarium number as follows:
1**1+ 7**2 + 5**3 = 1+ 49 + 125 = 175
"""
start=int(input("enter start interval:"))
end=int(input("enter end interval:"))
for i in range(start,end+1):
    temp=i
    num=i
    count=0
    while num>0:
        num=num//10
        count=count+1
    #print("number of digits in the number: ",count)
    num=temp
    sum=0
    for i in range(count,0,-1):
        rem=num%10
        #print(rem,"**",i)
        sum=sum+(rem**i)
        num=num//10
    #print(sum)
    if (temp==sum):
        print(temp)

"""
output:
enter start interval:1
enter end interval:1000
1
2
3
4
5
6
7
8
9
89
135
175
518
598

"""
