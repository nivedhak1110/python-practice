"""
2. Python program to interchange first and last elements in a list

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]
"""
list1= [12, 35, 9, 56, 24]
#interchange first and last element
print("Initial list:",list1)
length=len(list1)
list1[0],list1[length-1]=list1[length-1],list1[0]
print("After interchanging first and last element:",list1)
"""
Output:
Initial list: [12, 35, 9, 56, 24]
After interchanging first and last element: [24, 35, 9, 56, 12]
"""
