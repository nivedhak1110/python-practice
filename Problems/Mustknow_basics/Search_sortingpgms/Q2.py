"""
Q-2 Binary search
In the binary search algorithm, we can find the element position using 
the following methods.
1.Recursive Method
2.Iterative Method
"""
def binary_search(array,key):
    n=len(array)-1
    low=0
    high=n
    while low<=high:
        mid=(low+high)//2
        if array[mid]>key:
            high=mid-1
        elif array[mid]<key:
            low=mid+1
        elif array[mid]==key:
            return mid
        
    return -1
        
if __name__=='__main__':
    array=[1,2,3,4,5,6,7,8,9]
    key=int(input("enter the search key element:"))
    index=binary_search(array,key)
    if index==-1:
        print("{element} is not found in the array".format(element=key))
    else:
        print("{element} is present at position {position}".format(element=key,position=index+1))
"""
Output:
enter the search key element:5
5 is present at position 5
+++++
enter the search key element:56
56 is not found in the array
"""
