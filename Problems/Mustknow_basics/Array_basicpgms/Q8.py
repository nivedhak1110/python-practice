"""
Q-8
Python program to print the largest element in an array
"""
array=[10,20,90,270,6]
max=array[0]
for i in range(len(array)):
    if(array[i]>max):
        max=array[i]
print("largest element in the given array is {max}".format(max=max))
"""
Output:
largest element in the given array is 270
"""
