"""
Q-7
Python program to print all pronic numbers between 1 and 100
The pronic number is a product of two consecutive integers 
of the form: n(n+1).
Some pronic numbers are: 0, 2, 6, 12, 20, 30, 42, 56 etc.

For example:

6 = 2(2+1)= n(n+1),
72 =8(8+1) = n(n+1)"""
start=int(input("Enter start interval:"))
end=int(input("Enter end interval:"))
for i in range(start,end+1):
    temp=i
    num=i
    for j in range(1,num+1):
        if((j*(j+1))==num):
            print(num)
 """
 Output:
 Enter start interval:0

Enter end interval:100
2
6
12
20
30
42
56
72
90"""
