"""
3. Python | Ways to check if element exists in list
3.1 Linear search
3.2 Binary Search

#3.2this program uses Binary search technique to check if element exists in list
"""
def binary_search(array,key):
    length=len(array)
    low=0
    high=length-1
    while low<=high:
        mid=(low+high)//2
        if array[mid]==key:
            return mid
        elif array[mid]<key:
            low=mid+1
        elif array[mid]>key:
            high=mid-1
            
            
    return -1
    
if __name__=='__main__':
    array=[1,22,34,43,54,67,78,89,99,100]
    print("list:",array)
    key=int(input("enter a key to search in the list:"))
    search_result=binary_search(array,key)
    if search_result==-1:
        print("{key} is not present in the list {array}".format(key=key,array=array))
    else:
        print("{key} is present in the list {array} at position {position}".format(key=key,array=array,position=search_result+1))
"""
Output:
list: [1, 22, 34, 43, 54, 67, 78, 89, 99, 100]
enter a key to search in the list:99
is present in the list [1, 22, 34, 43, 54, 67, 78, 89, 99, 100] at position 9
****
list: [1, 22, 34, 43, 54, 67, 78, 89, 99, 100]
enter a key to search in the list:22
22 is present in the list [1, 22, 34, 43, 54, 67, 78, 89, 99, 100] at position 2
****
list: [1, 22, 34, 43, 54, 67, 78, 89, 99, 100]
enter a key to search in the list:3
3 is not present in the list [1, 22, 34, 43, 54, 67, 78, 89, 99, 100]
"""
