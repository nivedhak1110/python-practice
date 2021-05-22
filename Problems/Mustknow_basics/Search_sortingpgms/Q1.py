"""
Q-1
Linear search
Searching is a technique to find the particular element is present or not in the given list.
There are two types of searching -

Linear Search--->sequential search
Binary Search
"""
def linear_search(Array,key):
    for i in range(len(Array)):
        if A[i]==key:
            return i
    return -1
if __name__=='__main__':
    A=[12,23,3,44,52,100,34]
    key=int(input("enter the search element:"))
    index=linear_search(A,key)
    if index==-1:
        print("{element} is not found in the array".format(element=key))
    else:
        print("{element} is present at position {position}".format(element=key,position=index+1))
"""
Output:
enter the search element:4000
4000 is not found in the array
++++
enter the search element:12
12 is present at position 1
++++
enter the search element:44
44 is present at position 4
++++
enter the search element:100
100 is present at position 6
"""
