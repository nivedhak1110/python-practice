"""
Q-2 addition of two matrices
#taking A,B matrix as user input using list comprehension method

"""
#taking A,B matrix as user input
#take A matrix as user input
rows=int(input("enter the number of rows of A,B matrices:"))
cols=int(input("enter the number of cols of A,B matrices:"))
#method to take one line user input
print("Please enter row wise")
matrixA=[[int(input("enter matrixA element{i}{j}: ".format(i=i,j=j)))  for j in range(cols)] for i in range(rows)]
#important step to note to take input from users in one line
matrixB=[[int(input("enter matrixB element{i}{j}: ".format(i=i,j=j)))for j in range(cols)] for i in range(rows)]
#print matrix A and B
print("matrixA",matrixA)
print("matrixB",matrixB)
#Add matrix A,B
matrixC=[[0 for j in range(cols)] for i in range(rows)]
print("matrixC before adding matrixA,matrixB",matrixC)

for i in range(rows):
    for j in range(cols):
        matrixC[i][j]=matrixA[i][j]+matrixB[i][j]
print("matrixC",matrixC)
"""
Output:
enter the number of rows of A,B matrices:3
enter the number of cols of A,B matrices:3
Please enter row wise
enter matrixA element00: 1
enter matrixA element01: 1
enter matrixA element02: 1
enter matrixA element10: 2
enter matrixA element11: 2
enter matrixA element12: 2
enter matrixA element20: 3
enter matrixA element21: 3
enter matrixA element22: 3
enter matrixB element00: 1
enter matrixB element01: 1
enter matrixB element02: 1
enter matrixB element10: 2
enter matrixB element11: 2
enter matrixB element12: 2
enter matrixB element20: 3
enter matrixB element21: 3
enter matrixB element22: 3
matrixA [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matrixB [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matrixC before adding matrixA,matrixB [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrixC [[2, 2, 2], [4, 4, 4], [6, 6, 6]]

"""
