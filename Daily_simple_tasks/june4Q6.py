"""
6. pyramid * print 
"""
n=int(input("enter the number of rows:"))
m=2*n-1
for i in range(n+1):
    for j in range(m):
        print("",end=" ")
    for k in range(i):
        print("*",end=" ")
    m=m-1
    print(" ")
"""
output:
enter the number of rows:5

          
        *  
       * *  
      * * *  
     * * * *  
    * * * * * 

"""
