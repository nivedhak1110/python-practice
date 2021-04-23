#miscellaneous pattern-4
"""Pyramid of numbers less than 10
Pattern: 
1 
2 3 4 
5 6 7 8 9

   """
n=int(input("enter the number of rows: "))
k=1
stop=1
for i in range(n):
    for j in range(stop):
         print(k,end=" ")
         k=k+1
    stop=stop+2
    print()
     
