"""
2. pallindrome number
example:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202

"""
n=int(input("enter a number:"))
temp=n
rev=0
sum=0
while n>0:
    sum=n%10
    rev=(rev*10)+sum
    n=n//10
print("rev:",rev)
if(temp==rev):
    print("{temp} is a palindrome number".format(temp=temp))
else:
    print("{temp} is not a palindrome number".format(temp=temp))
"""
Output:
enter a number:2345
rev: 5432
2345 is not a palindrome number
******
enter a number:181
rev: 181
181 is a palindrome number
******
enter a number:1
rev: 1
1 is a palindrome number

"""
