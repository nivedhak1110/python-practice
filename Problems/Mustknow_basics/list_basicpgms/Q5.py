"""
Q-5
How to add two lists in Python
1.Add two lists using the Naive Method
2.Add two list using the Comprehension List
3.Add two list in Python using the map() function with add operator

(The map() function executes a specified function for each item in 
an iterable. 
The item is sent to the function as a parameter.
Syntax:
map(function, iterables))
"""
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
sum1=[]
#method1
for i in range(len(list1)):
    addition=list1[i]+list2[i]
    sum1.append(addition)
print("after list sum using for loop:",sum1)
#method2
sum2=[ x+y for (x,y) in zip(list1,list2)  ]
print("after list sum using for zip method:",sum2)
#method 3 
from operator import add #or write add function
sum3=list(map(add,list1,list2))
print("after list sum using for map method:",sum3)


"""
Output:
after list sum using for loop: [7, 9, 11, 13, 15]
after list sum using for zip method: [7, 9, 11, 13, 15]
after list sum using for map method: [7, 9, 11, 13, 15]

"""
    
