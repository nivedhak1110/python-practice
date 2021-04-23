"""
miscellaneous pattern-6
Pattern: –
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
"""
n=int(input("enter the number of rows: "))
stop=1
for i in range(1,n+1):
    for j in range(1,stop+1):
        if j<=i:
            print(j,end=" ")
            k=j-1
        else:
            print(k,end=" ")
            k=k-1
    stop=stop+2
"""
output:
enter the number of rows: 5
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 """
