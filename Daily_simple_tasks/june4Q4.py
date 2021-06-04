"""
4.fibonacci using recurison  
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,...
*****
F0 = 0 and F1 = 1
*****
                          fib(5)   
                     /                \
               fib(4)                fib(3)   
             /        \              /       \ 
         fib(3)      fib(2)         fib(2)   fib(1)
        /    \       /    \        /      \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /     \
fib(1) fib(0)
"""
def fibonacci(n):
    if n<0:
        print("please enter a positive number")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
    
if __name__=='__main__':
    n=int(input("number of terms of fibonacci required:"))
    for i in range(1,n+1):
        fib=fibonacci(i)
        print("{n}:{fib}".format(n=i,fib=fib))
"""
Output:
number of terms of fibonacci required:10
1:1
2:1
3:2
4:3
5:5
6:8
7:13
8:21
9:34
10:55
"""
