"""
3.fibonacci series without recursion
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ....
"""
terms=int(input("enter the number of terms required in the series:"))
n1=0
print(n1)
n2=1
print(n2)
i=0
while i<terms-2:
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    i=i+1
"""
Output:
enter the number of terms required in the series:10
0
1
1
2
3
5
8
13
21
34
"""
