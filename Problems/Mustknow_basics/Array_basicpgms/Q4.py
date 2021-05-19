"""
Q-4
Python program to print the duplicate elements of an array

"""
array=[1,2,2,3,3,4,5,7,8,8,8,7,7,10]
duplicate=[]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if(array[i]==array[j]):
            if array[i] not in duplicate:
                    duplicate.append(array[i])
 #print duplicate elements:
for i in range(len(duplicate)):
    print(duplicate[i])
"""
Output:
2
3
7
8
"""
