"""
Q-3 How to reverse a string in Python?
Python string library doesn't support the in-built "reverse()" 
function. But there are various ways to reverse the string. 
We are defining the following method to reverse the Python String.
1.Using for loop
2.Using while loop
3.Using the slice operator
4.Using the reversed() function
5.Using the recursion--->pending
"""
string=input("enter a string:")

#1.string reverse using for loop
#length=len(string)#len function can be used in string
rev1=""
for i in range(len(string)-1,-1,-1):
    rev1=rev1+string[i]#concatination of string
print("1.using for loop {string} is reversed as {rev1}".format(string=string,rev1=rev1))
#***********************
#2.using while loop
rev2=""
count=len(string)-1
while count>=0:
    rev2=rev2+string[count]
    count=count-1
print("2.using while loop {string} is reversed as {rev2}".format(string=string,rev2=rev2))
#********************** 
# 3.using slice operator
rev3=string[::-1]
print("3.using string slicing {string} is reversed as {rev3}".format(string=string,rev3=rev3))
"""
Explanation : The reversed() returns the reversed iterator 
of the given string and then its elements are joined empty 
string separated using join(). And reversed order string is 
formed.
"""
#*******************
#4.using reversed() function-->Required. Any iterable object
rev4="".join(reversed(string))
print("4.using reversed function {string} is reversed as {rev4}".format(string=string,rev4=rev4))
"""
Output:
enter a string:python
1.using for loop python is reversed as nohtyp
2.using while loop python is reversed as nohtyp
3.using string slicing python is reversed as nohtyp
4.using reversed function python is reversed as nohtyp


"""
