"""
Q-7
How to convert list to string in Python?
Method - 1
The given string iterates using for loop and adds its element to string variable.
method-2 
using join method-The join() method takes all items in an iterable and joins them into one string.
syntax: string.join(iterable)-->string-specified as separator


"""
#method1
list1=["python","programming","language"]
str1=""
for i in range(len(list1)):
    str1=str1+list1[i]+" "
print("list to string using for loop:",str1)
#method2
str2="#".join(list1)
print("list to string using join:",str2)
"""
Output:
list to string using for loop: python programming language 
list to string using join: python#programming#language
"""
