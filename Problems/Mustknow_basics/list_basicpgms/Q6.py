"""
Q-6
Understanding the difference between Lists and Sets:
lists-->ordered collection of datatypes
sets-->unordered collection of datatypes
The most significant difference between a set and a list in Python is that a set only stores unique items, whereas a list can consist of identical elements. For instance, suppose we have a list of mathematic test marks defined as "marks = [25, 30, 21, 19, 25, 27, 25, 17, 23, 20]", the list displays the user every value; however, when we convert the list into a set, it will remove the duplicates and leave {25, 30, 21, 19, 25, 27, 17, 23, 20}.

Another significant difference is that the sets use curly brackets, whereas the lists use square brackets.
"""
list1=[1,1,1,2,3,4,"python","program","program"]
print("List:",list1)
set1=set(list1)
print("Set:",set1)
"""
Output:
List: [1, 1, 1, 2, 3, 4, 'python', 'program', 'program']
Set: {1, 2, 3, 4, 'python', 'program'}
"""
