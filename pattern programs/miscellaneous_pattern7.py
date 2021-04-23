"""
miscellaneous pattern-7 Pattern double number on each column
Pattern:
0  
0  1  
0  2  4  
0  3  6   9  
0  4  8   12  16  
0  5  10  15  20  25  
0  6  12  18  24  30  36

"""
n=int(input("enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(j*i,end=" ")
    print()
"""
output:
enter the number of rows: 7
0 
0 1 
0 2 4 
0 3 6 9 
0 4 8 12 16 
0 5 10 15 20 25 
0 6 12 18 24 30 36 """
