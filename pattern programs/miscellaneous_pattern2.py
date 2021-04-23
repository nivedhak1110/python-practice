#miscellaneous pattern-2
"""Double the number pattern
   Pattern: –

   1 
   2    1 
   4    2    1 
   8    4    2    1 
  16    8    4    2    1 
  32   16    8    4    2    1 
  64   32   16    8    4    2    1 
 128   64   32   16    8    4    2    1 """
n=int(input("enter the number of rows: "))
for i in range(0,n):
    k=2**i
    for j in range(i+1):
         print(k,end=" ")
         k=int(k/2)
    print()
"""
Output:
enter the number of rows: 8
1 
2 1 
4 2 1 
8 4 2 1 
16 8 4 2 1 
32 16 8 4 2 1 
64 32 16 8 4 2 1 
128 64 32 16 8 4 2 1 """
