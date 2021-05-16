"""
Python program to left rotate the elements of an array

In this program, we need to rotate the elements of an array
towards the left by the specified number of times. In the left
rotation, each element of the array will be shifted to its 
left by one position and the first element of the array will 
be added to end of the list. This process will be followed
for a specified number of times.
12345---->array
n=1
23451---->after n left rotations 

"""
n=int(input("enter the number of left rotations:"))
A=[1,2,3,4,5]
print("original order of array elements")
for i in range(len(A)):
    print(A[i])
print("**********")
for i in range(n):
    for j in range(0,len(A)):
        if j!=0:
            A[j-1]=A[j]
            
        else:
            first=A[0]
            length=len(A)
            A[length-1]=first
            print(A[length-1])
            
print(" order of array elements after {n} left rotations".format(n=n))
for i in range(len(A)):
    print(A[i])
     
