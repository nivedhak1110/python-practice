"""
Q-9 Python program to print the smallest element in an array
"""
array=[120,6,60,17,300]
min=array[0]
for i in range(len(array)):
    if array[i]<min:
        min=array[i]
print("{min} is the smallest element in the array".format(min=min))
"""
Output:
6 is the smallest element in the array
"""
