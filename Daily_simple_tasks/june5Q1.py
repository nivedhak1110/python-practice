"""
1. Check armstrong number or not

A positive integer is called an Armstrong number of order n if
abcd... = a power n + b power n + c power n + d power n + ...
example:
1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, ...

"""

n= int(input("enter a number:"))
temp=n
count=0
if n==0:
    print("number of digits in the number:1")
else:
    while n>0:
        count=count+1
        n=n//10
    print("number of digits in the number:",count)
num=temp
add=0
i=0
while num>0:
    i=num%10
    add=add+(i**count)
    num=num//10
print("sum:",add)
if temp==add:
    print("{temp} is an armstrong number".format(temp=temp))
else:
    print("{temp} is not an armstrong number".format(temp=temp))

"""
Output:
enter a number:2
number of digits in the number: 1
sum: 2
2 is an armstrong number
*******
enter a number:15
number of digits in the number: 2
sum: 26
15 is not an armstrong number
*******
enter a number:123
number of digits in the number: 3
sum: 36
123 is not an armstrong number
*******
enter a number:153
number of digits in the number: 3
sum: 153
153 is an armstrong number
******
enter a number:9474
number of digits in the number: 4
sum: 9474
9474 is an armstrong number
********
enter a number:54748
number of digits in the number: 5
sum: 54748
54748 is an armstrong number
*******
"""
