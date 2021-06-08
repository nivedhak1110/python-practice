"""
4.1 Different ways to clear a(remove elements ) from list in Python
"""
#pop
array=[1,2,3,4,5,6]
print("Initial array:",array)
print("array.pop(1):")
array.pop(1)#pop(i) remove the element at index i, pop() by default removes last element
print(array)
#remove
print("array.remove(6):")#remove(i) removes element i from the list
array.remove(6)
print(array)
#del
print("del array[3]:")
del array[3]
print(array)
#clear
print("array.clear():")
array.clear()
print(array)
"""
output:
Initial array: [1, 2, 3, 4, 5, 6]
array.pop(1):
[1, 3, 4, 5, 6]
array.remove(6):
[1, 3, 4, 5]
del array[3]:
[1, 3, 4]
array.clear():
[]
"""
