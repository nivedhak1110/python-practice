"""
miscellaneous pattern-5
Pattern: –

10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2 """
n=int(input("enter the number of rows: "))

for i in range(1,n+1):
    k=10
    for j in range(i):
        print(k,end=" ")
        k=k-2
    print()
"""
output:
enter the number of rows: 5
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2 
"""
