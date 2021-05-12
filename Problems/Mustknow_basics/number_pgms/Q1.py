"""
Q-1
Python program to check if the given number is a Disarium 
Number
A number is said to be the Disarium number when the sum of its 
digit raised to the power of their respective positions 
becomes equal to the number itself.

For example, 175 is a Disarium number as follows:
1**1+ 7**2 + 5**3 = 1+ 49 + 125 = 175
"""
num=int(input("enter the number:"))
temp=num
count=0
while num>0:
    num=num//10
    count=count+1
print("number of digits in the number: ",count)
num=temp
sum=0
for i in range(count,0,-1):
    rem=num%10
    #print(rem,"**",i)
    sum=sum+(rem**i)
    num=num//10
#print(sum)
if (temp==sum):
    print("{temp}is a disarium number".format(temp=temp))
else:
    print("{temp}is not a disarium number".format(temp=temp))
"""
output:
enter the number:175
number of digits in the number:  3
175is a disarium number
*****
enter the number:89
number of digits in the number:  2
89is a disarium number
****
enter the number:25
number of digits in the number:  2
#27
25is not a disarium number
****

"""
