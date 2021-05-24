"""
Q-3
multiplication of two matrices taking user input
p*n X n*q-->p*Q[resultant matrix]
"""
#matrixA,matrix B input from user
p=int(input("enter the no of rows of matrixA:"))
n=int(input("enter the no of cols of matrixA/no of rows of matrix B:"))#must be equal inorder to perform matrix multiplication
q=int(input("enter the no of cols of matrixB:"))
matrixA=[[int(input("enter matrixA element{i}{j}: ".format(i=i,j=j))) for j in range(n)]for i in range(p)]
matrixB=[[int(input("enter matrixB element{i}{j}: ".format(i=i,j=j))) for j in range(q)]for i in range(n)]
matrixC=[[0  for j in range(q)]for i in range(p)]
print("matrixA",matrixA)
print("matrixB",matrixB)
print("matrixC before multipliction of matrixA and matrixB: ",matrixC)
#matrix multiplication
for i in range(p):#row number of matrixC to remember
    for j in range(q):#col numberof matrixC
        for k in range(n):#to traverse through each col of ith row in matrixA and to traverse through each row of jth colum of matrixB  ,that is why no of cols of matrixA/no of rows of matrix B are equal 
            matrixC[i][j]= matrixC[i][j]+ (matrixA[i][k]*matrixB[k][j])
print("matrixC after multipliction of matrixA and matrixB: ",matrixC)
"""
#Output:
2x2 matrixA,matrixB
enter the no of rows of matrixA:2
enter the no of cols of matrixA/no of rows of matrix B:2
enter the no of cols of matrixB:2
enter matrixA element00: 1
enter matrixA element01: 2
enter matrixA element10: 3
enter matrixA element11: 4

enter matrixB element00: 1
enter matrixB element01: 2
enter matrixB element10: 3
enter matrixB element11: 4
matrixA [[1, 2], [3, 4]]
matrixB [[1, 2], [3, 4]]
matrixC before multipliction of matrixA and matrixB:  [[0, 0], [0, 0]]
matrixC after multipliction of matrixA and matrixB:  [[7, 10], [15, 22]]
*************
3X3 matrixA and matrixB
enter the no of rows of matrixA:3
enter the no of cols of matrixA/no of rows of matrix B:3
enter the no of cols of matrixB:3
enter matrixA element00: 1
enter matrixA element01: 2
enter matrixA element02: 3
enter matrixA element10: 4
enter matrixA element11: 5
enter matrixA element12: 6
enter matrixA element20: 7
enter matrixA element21: 8
enter matrixA element22: 9
enter matrixB element00: 10
enter matrixB element01: 11
enter matrixB element02: 12
enter matrixB element10: 13
enter matrixB element11: 14
enter matrixB element12: 15
enter matrixB element20: 16
enter matrixB element21: 17
enter matrixB element22: 18
matrixA [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrixB [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
matrixC before multipliction of matrixA and matrixB:  [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrixC after multipliction of matrixA and matrixB:  [[84, 90, 96], [201, 216, 231], [318, 342, 366]]
"""
