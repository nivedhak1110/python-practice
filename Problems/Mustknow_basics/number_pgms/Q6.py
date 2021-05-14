"""
Q-6
Python program to print harshad number between 1 to 100
If a number is divisible by the sum of its digits, then it will 
be known as a Harshad Number.
"""
start=int(input("Enter start:"))
end=int(input("Enter end:"))
for i in range(start,end+1):
    temp=i
    num=i
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    #print(sum)
    if temp%sum==0:
        print(temp)
 """
 Output:
 Enter start:1
Enter end:100
1
2
3
4
5
6
7
8
9
10
12
18
20
21
24
27
30
36
40
42
45
48
50
54
60
63
70
72
80
81
84
90
100"""
