"""
Q-2 
Python program to find the frequency of each element in the 
array
Given array=[1  , 2,  8,  3 ,  2 ,  2,   2,   5,  1  ]

"""
A=[1,2,8,3,2,2,2,5,1 ]
Freq=[]
for i in range(len(A)):
    count=0
    for j in range(len(A)):
        if A[i]==A[j]:
            count=count+1
            
    Freq.append(count)
print("element|Frequency")
print("--------------------------")
for i in range(len(Freq)):
    print(A[i],"|",Freq[i])
print("--------------------------")
"""
Output:
element|Frequency
--------------------------
1 | 2
2 | 4
8 | 1
3 | 1
2 | 4
2 | 4
2 | 4
5 | 1
1 | 2
--------------------------
"""
