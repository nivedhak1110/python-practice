#Q-25 diamond pattern
n=int(input("enter the  number of rows:"))
m=2*n-2
for i in range(1,n+1):
    for j in range(1,m+1):
        print(end=" ")
    m=m-1
    for j in range(i):
            print("*",end=" ") 
    print()#by default new line
m=n-2
for i in range(n+1,0,-1):
    for j in range(1,m+1):
        print(end=" ")
    m=m+1
    for j in range(i):
        print("*",end=" ")
    print()
    """
    enter the  number of rows:5
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
    """
