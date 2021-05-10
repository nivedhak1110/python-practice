"""
Q-5
Python program to swap two variables,
using temporaray variable
"""
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
#Swap
temp=num1
num1=num2
num2=temp
#after swap
print("after swap num1:",num1)
print("after swap num2:",num2)
"""
Output:
enter num1:10
enter num2:20

after swap num1: 20
after swap num2: 10
"""
