"""
4.Python Program to Split the array and add the first part to the end
"""
array=[1,2,3,4,5,6,7,8]
print("Original array",array)
length=len(array)
mid=length//2
array1=array[0:mid]
print(array1)
array2=array[mid:length]
print(array2)
array3=array2+array1
print("Final array",array3)
"""
Output:
*****
Original array [1, 2, 3, 4, 5, 6, 7]
[1, 2, 3]
[4, 5, 6, 7]
Final array [4, 5, 6, 7, 1, 2, 3]
*****
Original array [1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4]
[5, 6, 7, 8]
Final array [5, 6, 7, 8, 1, 2, 3, 4]
"""
