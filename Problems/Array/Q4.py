"""
Q-4 find Equilibrium index of an array
Difficulty Level : Easy
Equilibrium index of an array is an index such that the sum 
of  elements at lower indexes is equal to the sum of 
elements at higher indexes.
(A[0] + A[1] + … + A[i-1]) = (A[i+1] + A[i+2] + … + A[n-1]) 
,where 0< i < n-1
For example, in an array A:
Input: A[] = {0, -3, 5, -4, -2, 3, 1, 0} 
Output:equilibrium index is found at [0,3,7] 
3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Input: A[] = {1, 2, 3} 
Output: -1 
"""
def equilibrium_index(array):
    
    leftsum=0
    rightsum=0
    equi=[]
    
    for i in range(len(array)):
        leftsum = 0
        rightsum = 0
        for j in range(i):
            leftsum=leftsum+array[j]
        for k in range(i+1,len(array)-1):
        	rightsum=rightsum+array[k]
        
        	
        if leftsum == rightsum:
            print("equilibrium index",i)
            equi.append(i)
    print(equi)
    return equi
if __name__ == '__main__':
    array=[0, -3, 5, -4, -2, 3, 1, 0]
    equilibrium_index(array)
    
    
    
"""
output:
equilibrium index 0
equilibrium index 3
equilibrium index 7
[0, 3, 7]
"""
