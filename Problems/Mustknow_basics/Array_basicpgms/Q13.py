"""
Q-13
Python program to sort the elements of an array in ascending
order
"""
array=[1,3,4,1000,21,32,98,100]
# print array before sorting
print("Before sorting:")
print(array)
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[j]<array[i]:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
#print the array after sorting in ascending order
print("array after sorting in ascending order:")
print(array)
"""
Output:

Before sorting:
[1, 3, 4, 1000, 21, 32, 98, 100]
array after sorting in ascending order:
[1, 3, 4, 21, 32, 98, 100, 1000]

"""
