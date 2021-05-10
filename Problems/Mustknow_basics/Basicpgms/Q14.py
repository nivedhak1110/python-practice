"""
Q-14
Python Program to Display the multiplication Table
"""
num=int(input("enter the number for which multiplication table need to be generated:"))
#table
for i in range (1,11):
    mul=i*num
    print("{i}*{num}={mul}".format(i=i,num=num,mul=mul))
"""
Output:
enter the number for which multiplication table need to be generated:4
1*4=4
2*4=8
3*4=12
4*4=16
5*4=20
6*4=24
7*4=28
8*4=32
9*4=36
10*4=40

"""
