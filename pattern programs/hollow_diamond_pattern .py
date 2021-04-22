#Q-26 hollow diamond pattern
n=int(input("enter the  number of rows:"))
m=2*n-2
for i in range(1,n+1):
    for j in range(1,m+1):
        print(end=" ")
    m=m-1
    for j in range(i):
        if j==0 or i-j==1: 
            print("*",end=" ") #row col
                               #1  0
                               #2  1 --->i-j==1
                                    
        else:
            print(" ",end=" ")
    print()#by default new line
m=n-2
for i in range(n+1,0,-1):
    for j in range(1,m+1):
        print(end=" ")
    m=m+1
    for j in range(i):
        if j==0 or i-j==1:     #row col
                               #6  5
                               #5  4 --->i-j==1
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    """
    Output:
    enter the  number of rows:5
        * 
       * * 
      *   * 
     *     * 
    *       * 
   *         * 
    *       * 
     *     * 
      *   * 
       * * 
        * 
    """
