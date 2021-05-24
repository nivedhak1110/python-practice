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
print("matrixB",matrixA)
print("matrixC before multipliction of matrixA and matrixB: ",matrixC)
#matrix multiplication
for i in range(p):#row number of matrixC to remember
    for j in range(q):#col numberof matrixC
        for k in range(n):#to traverse through each col of ith row in matrixA and to traverse through each row of jth colum of matrixB  ,that is why no of cols of matrixA/no of rows of matrix B are equal 
            matrixC[i][j]= matrixC[i][j]+ (matrixA[i][k]*matrixA[k][j])
print("matrixC after multipliction of matrixA and matrixB: ",matrixC)
