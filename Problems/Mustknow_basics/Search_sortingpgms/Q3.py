"""
Q-3 selection Sort in Python
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

"""
A=[10,3,1,32,45,667,21,42,111,285]
print("initial array:",A)
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if(A[j]<A[i]):
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
print("selection sort resultant array:",A)
"""
Output:
initial array: [10, 3, 1, 32, 45, 667, 21, 42, 111, 285]
selection sort resultant array: [1, 3, 10, 21, 32, 42, 45, 111, 285, 667]
"""
