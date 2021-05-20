"""
Q-1
How to append element in the list in python
1.append(elmt) - It appends the value at the end of the list.
2.insert(index, elmt) - It inserts the value at the specified index position.
3.extends(iterable) - It extends the list by adding the iterable object.
"""
list=[]
print("initial list",list)
list.append(3)
print("1.append method adds the element to the end of the list",list)
list.insert(0,10)#insert(index, elmt)
print("2. insert() inserts the value at the specified index position",list)
list.extend("python")
print("3. extend() extends the list by adding the iterable object",list)
"""
Output:
initial list []
1.append method adds the element to the end of the list [3]
2. insert() inserts the value at the specified index position [10, 3]
3. extend() extends the list by adding the iterable object [10, 3, 'p', 'y', 't', 'h', 'o', 'n']

"""
