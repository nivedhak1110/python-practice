"""
Q-1Python program to copy all elements of one array into 
another array

In this program, we need to copy all the elements of one 
array into another. This can be accomplished by looping 
through the first array and store the elements of the first 
array into the second array at the corresponding position."""
A=[1,2,3,4,5]
B=[]
#Print elements of original first array
for i in range(len(A)):
    print(A[i])
#copying
for i in range(len(A)):
    B.append(A[i])
print("****")
#print  second array
for i in range(len(B)):
    print(B[i])
"""
Output:
1
2
3
4
5
****
1
2
3
4
5  """  
