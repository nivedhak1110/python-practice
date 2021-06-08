"""
4.2 Python | Reversing a List (use built-in, slicing method)

"""
#method 1
list1=[1,2,3,4,5,6]
print("Initial list:",list1)
reversed_list1=list1[::-1]
print("Reversed list",reversed_list1)
#method 2
list2=[7,8,9,10]
print("Initial list:",list2)
reversed_list2=[]
for i in range(len(list2)-1,-1,-1):
    reversed_list2.append(list2[i])
print("Reversed list",reversed_list2)   

"""
Output:
Initial list: [1, 2, 3, 4, 5, 6]
Reversed list [6, 5, 4, 3, 2, 1]
Initial list: [7, 8, 9, 10]
Reversed list [10, 9, 8, 7]
"""
