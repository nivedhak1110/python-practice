"""
Q-12
Python program to sort the elements of an array in descending 
order
"""
array=[1,3,4,21,32,98,100]
# print array before sorting
print("Before sorting:")
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[j]>array[i]:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
#print the array after sorting in descending order
print(array)
"""
Output:
array after sorting in descending order
[100, 98, 32, 21, 4, 3, 1]
"""
