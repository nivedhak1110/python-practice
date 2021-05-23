"""
Q-5 Bubble sort in python
"""
array=[11,332,4,5,63,3,22]
print("Initial array:",array)
for i in range(len(array)-1,0,-1):
    for j in range(i):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print("Sorted array:",array)
"""
Output:
Initial array: [11, 332, 4, 5, 63, 3, 22]
Sorted array: [3, 4, 5, 11, 22, 63, 332]
Flow of execution:
Initial array: [11, 332, 4, 5, 63, 3, 22]
Sorted array: [11, 4, 5, 63, 3, 22, 332]#each iteration largest element will take its place and get fixed
Sorted array: [4, 5, 11, 3, 22, 63, 332]
Sorted array: [4, 5, 3, 11, 22, 63, 332]
Sorted array: [4, 3, 5, 11, 22, 63, 332]
Sorted array: [3, 4, 5, 11, 22, 63, 332]
Sorted array: [3, 4, 5, 11, 22, 63, 332]
"""
