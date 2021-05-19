"""
Q-3 How to reverse a string in Python?
Python string library doesn't support the in-built "reverse()" 
function. But there are various ways to reverse the string. 
We are defining the following method to reverse the Python String.

Using for loop
Using while loop
Using the slice operator
Using the reversed() function
Using the recursion
"""
string=input("enter a string:")
#1.string reverse using for loop
#length=len(string)#len function can be used in string
rev=""
for i in range(len(string)-1,-1,-1):
    rev=rev+string[i]#concatination of string
print("1.using for loop {string} is reversed as {rev}".format(string=string,rev=rev))
#2.using while loop
