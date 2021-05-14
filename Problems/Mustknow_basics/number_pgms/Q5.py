"""
Q-5
Python program to determine whether the given number is a 
Harshad Number.
If a number is divisible by the sum of its digits, then it will 
be known as a Harshad Number.
"""
num=int(input("Enter a number:"))
temp=num
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)
if temp%sum==0:
    print("{temp} is a Harshad number".format(temp=temp))
else:
    print("{temp} is Not a harshad number".format(temp=temp))
"""
Output:
****
Enter a number:24
6
24 is a Harshad number
****
Enter a number:25
7
25 is Not a harshad number
"""
