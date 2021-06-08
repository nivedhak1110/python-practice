"""
3. Python | Ways to check if element exists in list
3.1 Linear search
3.2 Binary Search

#3.1this program uses linear search technique to check if element exists in list
"""
def linear_search(list1,key):
    for i in range(len(list1)):
        if list1[i]==key:
            return i
    return -1
    
if __name__=='__main__':
    list1=[1,22,21,43,32,211]
    print("list:",list1)
    key=int(input("enter a key to search in the list:"))
    search_result=linear_search(list1,key)
    if search_result==-1:
        print("{key} is not present in the list {list1}".format(key=key,list1=list1))
    else:
        print("{key} is present in the list {list1} at position {position}".format(key=key,list1=list1,position=search_result+1))
"""
Output:
list: [1, 22, 21, 43, 32, 211]
enter a key to search in the list:211
211 is present in the list [1, 22, 21, 43, 32, 211] at position 6
****
list: [1, 22, 21, 43, 32, 211]
enter a key to search in the list:22
22 is present in the list [1, 22, 21, 43, 32, 211] at position 2
****
list: [1, 22, 21, 43, 32, 211]
enter a key to search in the list:2
2 is not present in the list [1, 22, 21, 43, 32, 211]
****
"""
