"""
Q-7
Python program to print the elements of an array present on 
odd position
pos   1 2 3 4 5
Array 1,2,3,4,5
index 0 1 2 3 4
"""
array=[1,2,3,4,5,6,7,8]
for i in range(0,len(array)):
    if i%2==0:#even idices-->odd positions
        print(array[i])
"""
Output:
1
3
5
7
"""
