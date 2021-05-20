"""
Q-2
How to compare two lists in Python
Python provides multiple ways to compare the two lists. 
Comparison is the process when the data items of are checked 
against another data item of list, whether they are the same 
or not.

The methods of comparing two lists are given below.

The cmp() function
The set() function and == operator
The sort() function and == operator
The collection.counter() function
The reduce() and map() function

list1 - [11, 12, 13, 14, 15]  
list2 - [11, 12, 13, 14, 15]  
Output - The lists are equal  
"""
A=[1,2,3,4,5,8]
B=[5,4,3,2,1]
equal=False
A.sort()
B.sort()
if A==B:
    print("the lists are equal")
else:
    print("lists are not equal")
"""
Output:
lists are not equal
"""
