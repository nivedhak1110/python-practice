"""
Q-16
Python Program to Check Armstrong Number
Armstrong number:
A positive integer is called an Armstrong number of order n if

abcd... = a power n + b power n + c power n + d power n + ...
In case of an Armstrong number of 3 digits, the sum of cubes 
of each digit is equal to the number itself. For example:

153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number."""
num=int(input("enter a number:"))
temp=num
count=0
while num>0:
    num=num//10
    count=count+1
print("number of digits in the number:",count)
    
num=temp
sum=0
while num>0:
    rem=num%10#remainder
    sum=sum+ (rem**count)
    num=num//10#quotient
    
#print(temp) 
#print(sum)
if(temp==sum):
    print("{temp} is an armstrong number".format(temp=temp))
else:
    print("{temp}is not armstrong number".format(temp=temp))
"""
Output:
enter a number:663
number of digits in the number: 3
663is not armstrong number
*****
enter a number:153
number of digits in the number: 3
153 is an armstrong number
*****
enter a number:371
number of digits in the number: 3
371 is an armstrong number
****
enter a number:8208
number of digits in the number: 4
8208 is an armstrong number
****
enter a number:1645
number of digits in the number: 4
1645is not armstrong number
"""
