"""
Q-3 Bubble Sort in Python

Concept of Bubble Sort:
The bubble sort uses a straightforward logic that works by repeating swapping the adjacent elements if they are not in the right order. It compares one pair at a time and swaps if the first element is greater than the second element; otherwise, move further to the next pair of elements for comparison.
"""
A=[10,3,1,32,45,667,21,42,111,285]
print("initial array:",A)
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if(A[j]<A[i]):
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
print("Bubble sort resultant array:",A)
"""
Output:
initial array: [10, 3, 1, 32, 45, 667, 21, 42, 111, 285]
Bubble sort resultant array: [1, 3, 10, 21, 32, 42, 45, 111, 285, 667]
"""
