"""
Q-1
take matrix input from user in python
#1.basic method
#2.one line method using list comprehension
"""
#Basic method to take and print matrix user input
rows=int(input("enter the num of rows of matrix:"))
cols=int(input("enter the num of cols of the matrix:"))
#initialize an entry matrix[--> implemented using lists in python]
matrix=[]
#enter values into matrix
for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(int(input("enter element {i}{j}: ".format(i=i,j=j))))
    matrix.append(a)
#printing values inside matrix
print("matrix:",matrix)
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
    print()
"""
#method 1 output:
enter the num of rows of matrix:3
enter the num of cols of the matrix:3
enter element 00: 1
enter element 01: 1
enter element 02: 1
enter element 10: 2
enter element 11: 2
enter element 12: 2
enter element 20: 3
enter element 21: 3
enter element 22: 3
matrix: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
1 1 1 
2 2 2 
3 3 3 
+++++
"""
