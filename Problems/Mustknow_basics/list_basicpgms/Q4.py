"""
Q-4
How to remove an element from a list in Python
Python provides the following methods to remove one or multiple 
elements. We can delete the elements using the del keyword by 
specifying the index position. Let's understand the following methods.

1.remove()-removes elements with specified value
2.pop()-removes element at the specified index,removes last element in the list if index not specified
3.clear()-removes all the elements from the list
4.del-del list[index] -->syntax 
5.List Comprehension - If specified condition is matched.
"""
list=[1,2,3,4,5,6,7,8,9,10]
print("Initial list:",list)
#remove
list.remove(4)
print("list after remove(4):",list )
#pop
list.pop()
print("list after pop():",list )
#del
del list[3]
print("list after list[3]:",list )
#list comprehension
#remove odd numbers
list=[x for x in list if x%2==0 ]
print("list after removing odd numbers using list comprehension:",list)
#clear-->removes all the elements
list.clear()
print("list after clear()",list)
"""
Output:

Initial list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list after remove(4): [1, 2, 3, 5, 6, 7, 8, 9, 10]
list after pop(): [1, 2, 3, 5, 6, 7, 8, 9]
list after list[3]: [1, 2, 3, 6, 7, 8, 9]
list after removing odd numbers using list comprehension: [2, 6, 8]
list after clear() []
"""
