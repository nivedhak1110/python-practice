#miscellaneous pattern-3
"""Pyramid of numbers up to 10
Pattern: 
1 
2 3 
4 5 6 
7 8 9 10

   """
n=int(input("enter the number of rows: "))
k=1
for i in range(n+1):
    for j in range(i):
         print(k,end=" ")
         k=k+1
    print()
