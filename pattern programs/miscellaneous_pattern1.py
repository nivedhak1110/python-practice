#More miscellaneous Patterns
#Q-32--Pyramid of horizontal number tables
"""
Pattern: 

1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
"""
#program
n=int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()
"""
output:
enter the number of rows: 10
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 """
