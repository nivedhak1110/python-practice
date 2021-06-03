"""
1. Write a program to swap 2 numbers. 
A- 99
B - 20
"""
#A=int(input("enter num1:"))
#B=int(input("enter num2:"))
A=99
B=20
print("intially A:",A)
print("intially B:",B)
#method 1 using temp
temp=A
A=B
B=temp
print("after swap A:",A)
print("after swap B:",B)
#method 2 without temp
C=999
D=200
print("intially C:",C)
print("intially D:",D)
C,D=D,C
print("after swap C:",C)
print("after swap D:",D)
"""
# Output:
*******

intially A: 99
intially B: 20
after swap A: 20
after swap B: 99
intially C: 999
intially D: 200
after swap C: 200
after swap D: 999

"""
