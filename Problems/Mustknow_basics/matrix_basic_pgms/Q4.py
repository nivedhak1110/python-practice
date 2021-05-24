"""
Q-4
Transpose of a matrix in python
matrixT= transpose of given matrix
"""
#take A matrix as user input
rows=int(input("enter the number of rows of A matrix:"))
cols=int(input("enter the number of cols of A matrix:"))
#method to take one line user input
print("Please enter row wise")
matrixA=[[int(input("enter matrixA element{i}{j}: ".format(i=i,j=j)))  for j in range(cols)] for i in range(rows)]
print("matrixA",matrixA)
#Initialize Transpose matrix 
matrixT=[[ 0 for j in range(rows)] for i in range(cols)]
for i in range(cols):
    for j in range(rows):
        matrixT[i][j]=matrixA[j][i]
print("matrixT",matrixT)  
"""
Output:
enter the number of rows of A matrix:3
enter the number of cols of A matrix:2
Please enter row wise
enter matrixA element00: 2
enter matrixA element01: 3
enter matrixA element10: 4
enter matrixA element11: 5
enter matrixA element20: 6
enter matrixA element21: 7
matrixA [[2, 3], [4, 5], [6, 7]]
matrixT [[2, 4, 6], [3, 5, 7]]
"""
